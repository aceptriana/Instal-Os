'jangan direcode ya icon tol'
from random import choice as ch
import os

link = ('https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh',
        'https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh',
        'https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Fedora/fedora.sh',
        'https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Parrot/parrot.sh',
        'https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh'
        )

uwu = (
        'kali.sh',
        'debian.sh',
        'fedora.sh',
        'parrot.sh',
        'ubuntu.sh'
        )

c = ("\033[1;31m","\033[1;32m","\033[1;33m","\033[1;34m","\033[1;35m","\033[1;36m")

info = os.uname()

cw = list(c)
def co():
    global cw
    if len(cw) == 0:
        cw += list(c)
    return cw.pop(ch(range(len(cw))))

os.system('clear')
print '''{a}
 ___           _        _ _                   _
|_ _|_ __  ___| |_ __ _| | | ___ _ __  __   _/ |
 | || '_ \/ __| __/ _` | | |/ _ \ '__| \ \ / / |
 | || | | \__ \ || (_| | | |  __/ |     \ V /| |
|___|_| |_|___/\__\__,_|_|_|\___|_|      \_/ |_|
{b}Author: {c}Acep X-Code
{b}Creator: {c}Mayat 2.7.15
{der}
{d}1. Linux
2. Debian
3. Fedora
4. Parrot OS
5. Ubuntu
{der}
'''.format(der="\033[0;1m"+'#'*40, a=co(), b=co(), c=co(), d=co())

try:
    yey = input('%s%s@%s:# %s'%(co(), info[1], info[0], co()))
    yey -= 1 if (yey > 0 < 6) else exit()
    os.system('hash -r && wget {a} && bash {b} && chmod +x start-{b} && ./start-{b}'.format(a=link[yey], b=uwu[yey]))
except:
    exit()
