
"""

            author: @Hacknology
            contact: utkucolak05@gmail.com
            date: 27.05.2017
"""
import urllib2
import sys
import time
import re
import requests
from colorama import Fore, Back, Style, init
red     = Fore.RED
cyan    = Fore.CYAN
blue    = Fore.BLUE
green   = Fore.GREEN
white   = Fore.WHITE
yellow  = Fore.YELLOW
magenta = Fore.MAGENTA
bright  = Style.BRIGHT
sqliErrors = {
			 "error in your SQL syntax": 'SQL syntax error',
			 "Query failed": 'Query failed',
			 "supplied argument is not a valid MySQL result resource in": 'Bad argument',
			 "Microsoft JET Database Engine error '80040e14'": 'JET DBE error',
			 "Error:unknown": 'Unknown error',
			 "Fatal error": 'Fatal error',
			 "mysql_fetch": 'MySQL fetch',
			 "Syntax error": 'Syntax error'
			}
def control_sql(f):
    
    dosya = open(f, "r+").readlines()

    for url in dosya:
        url.strip()
        new = url + "'"
        req = requests.get(new)
        for hata in sqliErrors:
            if hata in req.content:
                print bright + green + url + 'may be vulnareble!'
        
                
                
                
