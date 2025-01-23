from mitmproxy import http
import threading
import re
from queue import Queue
import base64
from collections import Counter
import datetime
import time
import random
import yara

# mitmproxy --set filter="~u cs.tru.ca" -s networkmon.py


# net_rules = yara.compile(filepath="net_rules.yar")
# header_checks = {'Host' ,'Referer', 'Cookie', 'Accept-Language', 'User-Agent', 'Accept-Encoding', 'Connection', 'Upgrade-Insecure-Requests', 'Cache-Control'}# Many malware sample might not include referer or cookie values which might be suspicious
bad_tlds = {"tk","xyz", 'pe', 'vg', 'ru',"ga","ml","cf","gq", "onion", 'ca'} # Well know tlds associated with malware campaigns

bad_commands_pattern = r'\b(?:' + '|'.join(re.escape(command) for command in [
        'eval', 'exec', 'powershell.exe', 'cmd.exe', 'subprocess', 'curl',
        'bitsadmin', 'run', 'Popen', 'wget', 'shell', 'powershell', 'Invoke-WebRequest',
        'cmd', 'shutdown', 'nc', 'bash', 'sudo', 'ssh', 'telnet', 'proc_open',
        'shell_exec', 'wmic', 'Invoke-Command', 'dir', 'ls', 'pwd', 'del',
        'ifconfig', 'ipconfig', 'netstat', 'Invoke-Expression', 'schtasks', 'rundll32'
]) + r')\b'

bad_command_regex = re.compile(bad_commands_pattern, re.IGNORECASE)
x_pattern = re.compile(r'^X-.*', re.IGNORECASE)

log_queue = Queue(maxsize=40)

def collect_logs():
    while True:
        if not log_queue.empty():
            log_data = log_queue.get()
            with open("mon_data.txt", 'a') as l:
                l.write(log_data)
            log_queue.task_done()
        else:
            time.sleep(random.randint(3,7))

# Start the log collection thread
thread_l = threading.Thread(target=collect_logs)
thread_l.daemon = True  # Daemonize the thread so it will exit when the main program exits
thread_l.start()

# def clean_content(content):
#     tag_re = re.compile(r'<(h[1-6]|p|span|div|footer|header|section|article|aside|nav|main|figure|figcaption|strong|em|b|i|u|small|br|hr|ol|ul|li|table|tr|td|th|thead|tbody|tfoot|a|img|input|button|form|label)[^>]*>', re.IGNORECASE)
#     clean_content = tag_re.sub('', content)
#     return clean_content.strip()

# This method will try to detect base64 payloads and decrypt them in real time
def check_base64_pattern(con):
    global log_queue
    try:
        decoded_data = base64.b64decode(con, validate=True)
        dat = decoded_data.decode('utf-8')
        log_queue.put("\n[ALERT] Base64 encoding found!\n")
        return dat
    except (base64.binascii.Error, UnicodeDecodeError):
        return con

# This methos will check if the requests from any executable or browser is to a trusted domain list or not
def check_suspicious_host(dat, method):
    global log_queue
    global bad_tlds
    if method == "GET":
        print(dat.pretty_url)
        log_queue.put(f"GET DETECTED to {dat.pretty_url}\n\n", block=False)
    elif method == "POST":
         log_queue.put_nowait(f"POST DETECTED to {dat.pretty_url} \n\n")
    curr_dom = dat.pretty_host.split('.')[-1].lower()
    if curr_dom in bad_tlds:
        log_queue.put_nowait(f'\n[ALERT] Suspicious TLD found: {curr_dom}\n')
    if any(host in dat.pretty_host.split('.')[0].lower() for host in ['pastebin', 'discord', 'tinyurl']):
        log_queue.put_nowait(f"\n\n[ALERT] Possible botnet or phishing operation [REASON]: {dat.pretty_host}\n\n")
    
# This method will check if a application or compiled file is being donwloaded
def check_if_mal_file(full_url):
    global log_queue
    if full_url.endswith('.exe') or full_url.endswith('.dll') or full_url.endswith('.bat') or full_url.endswith('.psl'):
        log_queue.put(f"\n[Alert] Dangerous file download detected\n", block=False)

def check_X_headers(headers):
    global x_pattern
    for header, value in headers.items():
        if x_pattern.match(header):
            log_queue.put(f'\n\nUncommon- {header}:{value}\n\n')
            
def check_command_patterns(dat):
    global bad_command_regex
    global log_queue
    val = bool(bad_command_regex.search(dat))
    if val:
        log_queue.put("\n[ALERT] Remote code execution detected\n", block=False)
        
def request(flow: http.HTTPFlow) -> None:
    global log_queue
    if flow.request.method == 'GET':
        if any(str.lower() in flow.request.pretty_url for str in ['microsoft', 'login.live', 'bing', 'cdn', 'vscode']):
            pass
        else:
            u_agent = flow.request.headers.get('User-Agent', '').lower()  # Convert to lowercase for case-insensitive comparison

            if any(browser in u_agent for browser in ['chrome', 'edge', 'firefox', 'microsoft']):
                pass
            else:
                c_time = datetime.datetime.now()
                log_queue.put(f"***************************************************\n\nTimestamp: {c_time.strftime('%I:%M:%S %p')}\n\n", block=False)
                check_suspicious_host(flow.request, 'GET')
                check_if_mal_file(flow.request.pretty_url)

    elif flow.request.method == "POST":
        p_agent = flow.request.headers.get('User-Agent', '').lower()  # Convert to lowercase for case-insensitive comparison
        if any(browser in p_agent for browser in ['chrome', 'edge', 'firefox', 'safari']):
            pass
        else:
            c_time = datetime.datetime.now()
            log_queue.put(f"***************************************************\n\nTimestamp: {c_time.strftime('%I:%M:%S %p')}\n\n")
            check_suspicious_host(flow.request, 'POST')
            check_X_headers(flow.request.headers)
            if 'application/octet-stream' in flow.request.headers.get('Content-Type', ''):
                log_queue.put(f"Exfilteration detected\n", block=False)
            if len(flow.request.content.decode('utf-8').strip())/1024 > 10:
                log_queue.put(f"Large Request Data: {flow.request.content.decode('utf-8').strip()/1024} kb", block=False)
            p_dat = check_base64_pattern(flow.request.content.decode('utf-8'))
            log_queue.put(f"\nPayload: {p_dat}\n", block=False)

def response(flow: http.HTTPFlow) -> None:
    global log_queue
    if flow.request.method == 'GET':
        if flow.response.status_code == 200:
            u_agent = flow.request.headers.get('User-Agent', '').lower()  # Convert to lowercase for case-insensitive comparison
            c_type = flow.request.headers.get('Content-Type', '').lower() 
            if any(browser in u_agent for browser in ['chrome', 'edge', 'firefox', 'Microsoft']) or "application/x-msdos-program" in c_type:
                pass
            else:
                final_string = ''
                if flow.response.content.decode().strip() == '':
                    final_string += '\n********************************************************************************\n\n'
                else:
                    check_b64 = check_base64_pattern(flow.response.content.decode())
                    check_command_patterns(check_b64)
                    log_queue.put('\n\nGET RESPONSE\n\n')
                    if len(flow.response.content)/1024 <= 50 and len(flow.response.content)/1024 >= 6:
                        log_queue.put(f'Large Payload Detected\n\n', block=False)
                    log_queue.put(f"\nPayload: {check_b64}\n\n", block=False)
        elif flow.response.status_code == 404:
            log_queue.put(f"\nError getting the data, 404 error\n")
