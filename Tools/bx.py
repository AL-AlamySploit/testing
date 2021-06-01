import sys
import time
import random
import os
from gtts import gTTS
######################################################################
d=['\033[1;30m' , '\033[1;32m' , '\033[1;33m' , '\033[1;34m' , '\033[1;35m' , '\033[1;36m' , '\033[1;37m']
#####################################################################
def jalan(x):
	for e in x + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.01)
#####################################################################
os.system('clear')
os.system('pip install gTTS')
os.system('pkg install mpv -y')
os.system('clear')
os.system("git pull https://github.com/khalid-bx/hak-bx")
os.system('clear')
print(random.choice(d))
jalan("──────╔═══╗╔╗───╔═══╗╔═══╗╔═╗╔═╗")
jalan("──────║╔══╝║║───║╔═╗║║╔═╗║║║╚╝║║")
jalan("╔╗╔╗╔╗║╚══╗║║───║║─╚╝║║─║║║╔╗╔╗║")
jalan("║╚╝╚╝║║╔══╝║║─╔╗║║─╔╗║║─║║║║║║║║")
jalan("╚╗╔╗╔╝║╚══╗║╚═╝║║╚═╝║║╚═╝║║║║║║║")
jalan("─╚╝╚╝─╚═══╝╚═══╝╚═══╝╚═══╝╚╝╚╝╚╝")
ine=input("\033[1;33mWHAT IS YOUR NAME : ")
tx=(ine+"welcome to script khalid bx")
lan="en"
uot=gTTS(text=tx,lang=lan,slow=False)
uot.save("xo.mp3")
os.system('mpv xo.mp3')
time.sleep(0.3)
os.system('clear')
######################################################################
m=['\033[1;32m' , '\033[1;31m' , '\033[1;33m' , '\033[1;34m' , '\033[1;35m' , '\033[1;36m' , '\033[1;36m']
######################################################################
print(random.choice(m))
logo="""
'##:::'##:'##::::'##::::'###::::'##:::::::'####:'########::
 ##::'##:: ##:::: ##:::'## ##::: ##:::::::. ##:: ##.... ##:
 ##:'##::: ##:::: ##::'##:. ##:: ##:::::::: ##:: ##:::: ##:
 #####:::: #########:'##:::. ##: ##:::::::: ##:: ##:::: ##:
 ##. ##::: ##.... ##: #########: ##:::::::: ##:: ##:::: ##:
 ##:. ##:: ##:::: ##: ##.... ##: ##:::::::: ##:: ##:::: ##:
 ##::. ##: ##:::: ##: ##:::: ##: ########:'####: ########::
..::::..::..:::::..::..:::::..::........::....::........:::"""
logo2="""
'########::'##::::'##:
 ##.... ##:. ##::'##::               
 ##:::: ##::. ##'##:::       
 ########::::. ###::::        Welcome to my tool 
 ##.... ##::: ## ##:::       
 ##:::: ##:: ##:. ##::
 ########:: ##:::. ##:
........:::..:::::..::"""
time.sleep(00000.01)

def awamir():
	print("\033[1;36m[1] \033[1;32minstall all pkg termux")
	time.sleep(0.3)
	print("\033[1;36m[2] \033[1;32mUpdate && upgrade termux")
	time.sleep(0.3)
	print("\033[1;36m[3] \033[1;32mhack android")
	time.sleep(0.3)
	print("\033[1;36m[4] \033[1;32minstall metasploit")
	time.sleep(0.3)
	print("\033[1;36m[5] \033[1;32minstall ngrok")
	time.sleep(0.3)
	print("\033[1;36m[6] \033[1;32mGiving root permissions to Termux")
	time.sleep(0.3)
	print("\033[1;36m[7] \033[1;32mMy account on Facebook")
	time.sleep(0.3)
	print("\033[1;36m[0] \033[1;32mEXIT")
##################################################
print(logo)
print(logo2)
print()
awamir()
#########################################################################################
chosse = input("\033[1;35mChosse an option : ")
if chosse=='1':
	os.system('pkg update && upgrade -y ;pip install --upgrade pip ; pkg install git -y ; pkg install nano -y ; pkg install python -y ; pkg install python2 -y ; pkg install php -y;pkg install unzip -y ; pkg install openssh -y ; pkg install cat -y ; pkg install curl -y ; pkg install wget -y ; pkg install w3m -y ;pkg install golang -y ; pkg install havij -y ; pkg install db -y ; pkg install postgresql -y ; pkg install uftrace -y ; pkg install ruby -y ; pkg install perl -y; pkg install bash -y ;pkg install figlet -y;pkg install cowsay -y; pkg install tar -y;pkg install zip -y; pkg install tor -y; pkg install toilet -y;pkg install proot -y; pkg install golang -y; pkg install openssl -y;pkg install cmatrix -y ; pkg install macchanger ;pkg install root-repo -y;pkg install unstable-repo -y;pkg install x11-repo -y ; pip install --upgrade pip ; python bx.py ')
elif chosse=='2':
	jalan("plase waith...")
	os.system('apt update && apt upgrade -y && python bx.py')
elif chosse=='3':
    os.system('apt update && apt upgrade && git clone https://github.com/cyberknight777/PhoneSploit && cd PhoneSploit && bash termux.sh')
elif chosse=='4':
	os.system('pkg install root-repo ; pkg install unstable-repo ; pkg install x11-repo ; pkg update && pkg upgrade && pkg install git curl wget nmap -y && curl -LO raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh && chmod 777 metasploit.sh && ./metasploit.sh ; bash metasploit.sh')
elif chosse=='5':
	os.system('apt update && apt upgrade -y && git clone https://github.com/tchelospy/termux-ngrok.git && cd termux-ngrok && chmod +x termux-ngrok.sh && ./termux-ngrok.sh')
elif chosse=='6':
	os.system('apt update && apt -y upgrade && pkg install -y git && pkg install -y proot && termux-setup-storage && git clone https://github.com/Anonymous-Zpt/T-root && cd T-root && bash install.sh')
elif chosse=='7':
	os.system('xdg-open https://www.facebook.com/khaled.fidel.1800')
elif chosse=='0':
	os.system('exit')
else:
    jalan("\033[1;31mplease chosse just 1 or 2 or 3 or 4 or 5 or 6 okay bro")
    os.system('python bx.py')