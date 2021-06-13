import os
from time import sleep


p ='\033[0;35m'
b ='\033[0;34m'
y ='\033[0;33m'

def setup():
    try:
        os.mkdir('/data/data/com.termux/files/home/.termux')
    except:
        pass
    key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
    open('/data/data/com.termux/files/home/.termux/termux.properties','w').write(key)
    os.system('termux-reload-settings')


def banner():
    os.system('clear')
    print(p+'ﺕﺍﺭﺎﺼﺘﺧﻻﺍ ﺔﻓﺎﺿﺍ ﺓﺍﺩﺍ'.center(40))
    print(y+' HK Hacker :ﻢﻴﻤﺼﺗ'.center(40))
    print("".join([i for i in "\n"*3]))


if __name__=='__main__':
    banner()
    from threading import Thread as td
    t = td(target=setup)
    t.start()
    while t.is_alive():
        for i in "-\|/-\|/":
            print('\rﺮﻈﺘﻧﺍ '+i+' ',end="",flush=True)
            sleep(0.1)
    banner()
    print (b+' ^_^  ﻊﺘﻤﺘﺳﺍ ,ﺕﺍﺭﺎﺼﺘﺧﻻﺍ ﺔﻓﺎﺿﺍ ﻢﺗ')

# shortcut
# HK Hacker
