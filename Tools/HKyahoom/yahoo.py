# 67coded by Yutix
# totality free, not for sale
# recoder anak anjing!

import requests as req
import requests.exceptions as rx
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor as tpx

grey = '\033[90m'
red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[94m'
purple = '\033[95m'
cyan = '\033[96m'
white = '\033[37m'
off = '\033[m'
vuln = []

def validator(email):
	try:
		yid = email.split('@')[0]
		url = 'https://login.yahoo.com/account/create'
		ses = req.Session()
		raw = ses.get(url,timeout=30).text
		frm = bs(raw,'html.parser').find('form')
		uri = frm['action']
		tok = frm.findAll('input')
		dat = { "browser-fp-data":"",
				"specId":"yidreg",
				"cacheStored":"",
				"crumb":tok[3]['value'],
				"acrumb":tok[4]['value'],
				"sessionIndex":tok[5]['value'],
				"done":"https%3A%2F%2Fwww.yahoo.com",
				"googleIdToken":"",
				"authCode":"",
				"attrSetIndex":"0",
				"tos0":"oath_freereg%7Cid%7Cid-ID",
				"firstName":"Yutix",
				"lastName":"Yutixcode",
				"yid":yid,
				"password":"Yutixcode1997",
				"shortCountryCode":"ID",
				"phone":"82321062760",
				"mm":"5",
				"dd":"25",
				"yyyy":"1997",
				"freeformGender":"",
				"signup":"" }
		res = ses.post(uri,data=dat,timeout=30).text
		pns = bs(res,'html.parser').find('div',{'class':'oneid-error-message'})
		
		if pns != None:
			print(f'{white}[{red}ﺡﺎﺘﻣ ﺮﻴﻏ{white}]{red} {email}')
		else:
			print(f'{white}[{green}ﺡﺎﺘﻣ{white}]{green} {email}')
			vuln.append(email)
			
	except rx.ReadTimeout:
		print(f'{white}[{red}....{white}]{red} {email}{white} |{red} ﺔﻠﻬﻤﻟﺍ ﺖﻬﺘﻧﺍ')
	except rx.ConnectionError:
		print(f'{white}[{red}....{white}]{red} {email}{white} |{red} ﻝﺎﺼﺗﻻﺍ ﻲﻓ ﺄﻄﺧ')

def multi(path):
	print()
	with open(path,'r') as mail:
		with tpx(max_workers=20) as crot:
			lines = mail.readlines()
			for line in lines:
				crot.submit(validator,line.strip())
	print(f'{white}\nﺡﺎﺘﻣ: {green}{len(vuln)}')
	print(f"{white}ﻒﻠﻣ ﻲﻓ ﺕﺎﺣﺎﺘﻤﻟﺍ ﻆﻔﺣ ﻢﺗ: {green}'vuln.txt'")
	for maill in vuln:
		with open('vuln.txt','a') as vulnsave:
			vulnsave.write(f'{maill}\n')

def main():
	print(f'\n {yellow}_   _ _  _ ____ _ _    {white}____ _  _ ____ ____ _  _ \n {yellow} \_/  |\/| |__| | |    {white}|    |__| |___ |    |_/  \n {yellow}  |   |  | |  | | |___ {white}|___ |  | |___ |___ | \_ \n\n   HK Hacker : ﻢﻴﻤﺼﺗ\n     ﻮﻫﺎﻳ ﺡﺎﺘﻣ ﺺﺤﻓ\n\n{purple}[١]{white}ﺪﺣﺍﻭ ﺪﻳﺮﺑ ﺺﺤﻓ\n{purple}[٢]{white}ﺪﻳﺮﺑ ﻦﻣ ﺮﺜﻛﺍ ﺺﺤﻓ')
	menu = input(f'   > ')
	if menu == '1' or menu == '١':
		validator(input(f'\n{white}(123 ﻂﻘﻓ ﻭﺍ 123@yahoo.com:لﺎﺜﻣ) ﺪﻳﺮﺒﻟﺍ:{yellow} '))
	elif menu == '2' or menu == '٢':
		multi(input(f'\n{white}(example.txt وأ /sdcard/emails.txt :لﺎﺜﻣ) ﻒﻠﻤﻟﺍ ﺭﺎﺴﻣ:{yellow} '))
	else:
		exit(f'\nﺝﻭﺮﺧ')

if __name__=='__main__':
	main()
