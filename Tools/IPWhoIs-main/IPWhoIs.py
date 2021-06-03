#!/usr/bin/env python3
# Author: @haithamaouati
# Version:1.0

import argparse
import colorama
import os
import urllib2
import json

from colorama import Fore, Back, Style
colorama.init()

os.system('cls' if os.name == 'nt' else 'clear')

print('''\

  __     ______   __     __     __  __     ______     __     ______    
 /\ \   /\  == \ /\ \  _ \ \   /\ \_\ \   /\  __ \   /\ \   /\  ___\   
 \ \ \  \ \  _-/ \ \ \/ ".\ \  \ \  __ \  \ \ \/\ \  \ \ \  \ \___  \  
  \ \_\  \ \_\    \ \__/".~\_\  \ \_\ \_\  \ \_____\  \ \_\  \/\_____\ 
   \/_/   \/_/     \/_/   \/_/   \/_/\/_/   \/_____/   \/_/   \/_____/ 
''')

print('Author: ' + Fore.CYAN + '@haithamaouati' + Fore.WHITE + ' Version: ' + Fore.YELLOW + '1.0\n' + Fore.WHITE)

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip', metavar='<ip>', type=str, help='IP used for the query (e.g. 8.8.4.4)')

args = parser.parse_args()

if args.ip == None:
	parser.print_help()
	exit();
ip = args.ip

# Sending an API request
response = urllib2.urlopen("http://ipwhois.app/json/"+ip)
ipgeolocation = json.load(response)

# Country code output, field "country_code"

print Fore.WHITE + 'IP Address: ' + Fore.GREEN + ipgeolocation["ip"]
print Fore.WHITE + 'IP Address Type: ' + Fore.GREEN + ipgeolocation["type"]
print Fore.WHITE + 'Continent Name: ' + Fore.GREEN + ipgeolocation["continent"]
print Fore.WHITE + 'Continent Code: ' + ipgeolocation["continent_code"]
print Fore.WHITE + 'Country Name: ' + Fore.GREEN + ipgeolocation["country"]
print Fore.WHITE + 'Country Code: ' + Fore.GREEN + ipgeolocation["country_code"]
print Fore.WHITE + 'Country Capital: ' + Fore.GREEN + ipgeolocation["country_capital"]
print Fore.WHITE + 'Country Phone Code: ' + Fore.GREEN + ipgeolocation["country_phone"]
print Fore.WHITE + 'Neighboring Countries: ' + Fore.GREEN + ipgeolocation["country_neighbours"]
print Fore.WHITE + 'Region/State: ' + Fore.GREEN + ipgeolocation["region"]
print Fore.WHITE + 'City: ' + Fore.GREEN + ipgeolocation["city"]
print Fore.WHITE + 'Latitude: ' + Fore.GREEN + ipgeolocation["latitude"]
print Fore.WHITE + 'Longitude: ' + Fore.GREEN + ipgeolocation["longitude"]
print Fore.WHITE + 'ASN number: ' + Fore.GREEN + ipgeolocation["asn"]
print Fore.WHITE + 'Organization Name: ' + Fore.GREEN + ipgeolocation["org"]
print Fore.WHITE + 'ISP Name: ' + Fore.GREEN + ipgeolocation["isp"]
print Fore.WHITE + 'City TimeZone: ' + Fore.GREEN + ipgeolocation["timezone"]
print Fore.WHITE + 'Time Zone: ' + Fore.GREEN + ipgeolocation["timezone_name"]
print Fore.WHITE + 'TimeZone daylight-savings: ' + Fore.GREEN + ipgeolocation["timezone_dstOffset"]
print Fore.WHITE + 'TimeZone UTC: ' + Fore.GREEN + ipgeolocation["timezone_gmtOffset"]
print Fore.WHITE + 'Timezone GMT: ' + Fore.GREEN + ipgeolocation["timezone_gmt"]
print Fore.WHITE + 'Country Currency Name: ' + Fore.GREEN + ipgeolocation["currency"]
print Fore.WHITE + 'Country Currency Code: ' + Fore.GREEN + ipgeolocation["currency_code"]