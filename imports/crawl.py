"""

            author: @Hacknology
            contact: utkucolak05@gmail.com
            date: 28.05.2017
"""

import requests,re,sys
from mechanize import Browser
import google
from colorama import Fore, Back, Style, init

red     = Fore.RED
cyan    = Fore.CYAN
blue    = Fore.BLUE
green   = Fore.GREEN
white   = Fore.WHITE
yellow  = Fore.YELLOW
magenta = Fore.MAGENTA
bright  = Style.BRIGHT
br=Browser()
dorks = []
links = []
def get_title(url, sayfa=3):
    br.open(url)
    title = br.title().split()
    
    for word in title:
        dork = "inurl:{}.php?id=".format(word)
        dorks.append(dork)
    try:
        for ara in dorks:
        
            search = google.search(ara, stop=3)
            for x in search:
                yaz = open("new_url.txt", "a+")
                yaz.write(x + "\n")
                
    except Exception as e:
        print "[-]An error has occurred. Try other sites or use VPN"
        sys.exit()
    print bright + green + "[+]Check the .txt file!"
    
    
    
        
        
            
    
