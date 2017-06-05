logo = """
  |\     /|(  ___  )( \      |\     /|(  ___  )( \      ( \      (  ___  )
  | )   ( || (   ) || (      | )   ( || (   ) || (      | (      | (   ) |
  | |   | || (___) || |      | (___) || (___) || |      | |      | (___) |
  ( (   ) )|  ___  || |      |  ___  ||  ___  || |      | |      |  ___  |
   \ \_/ / | (   ) || |      | (   ) || (   ) || |      | |      | (   ) |
    \   /  | )   ( || (____/\| )   ( || )   ( || (____/\| (____/\| )   ( |
     \_/   |/     \|(_______/|/     \||/     \|(_______/(_______/|/     \|

                                             Hacknology
                                             https://github.com/Hacknology/
                                             "Hammer of hate is our faith"

    """
import warnings
import sys
warnings.filterwarnings('ignore')
from imports import scan_site,sqltest,crawl,wp_brute
from colorama import Fore, Back, Style, init

red     = Fore.RED
cyan    = Fore.CYAN
blue    = Fore.BLUE
green   = Fore.GREEN
white   = Fore.WHITE
yellow  = Fore.YELLOW
magenta = Fore.MAGENTA
bright  = Style.BRIGHT
print bright + blue + logo
def help():
    print yellow + """
\t\t\tCommands:
\t\t\t\tscan site: Scan wordpress sites online.
\t\t\t\thelp: Show this message
\t\t\t\texit: Quit
\t\t\t\ttest sqli: Test all the link that you gave in .txt file if they are vulnerable
\t\t\t\tbrute: Make brute force attack to wordpress site.
\t\t\t\tcrawler: Find new sites with keywords of sites that you gave before.
"""
while True:
    komut = raw_input(bright + green + "\ncommand => ").lower()
    if komut == "scan site":
        scan_site.create_word()
        scan_site.create_dork(5)
        scan_site.wp_get_query(10)
    elif komut == "help":
        help()
    elif komut == "exit":
        sys.exit()
    elif komut == "test sqli":
        sqltest.control_sql(f=raw_input(bright+yellow+"File: "))
    elif komut == "crawler":
        dosya = open(raw_input(bright+yellow+"Please give the filename of url list: "), "r+").readlines()
        try:
            for url in dosya:
                crawl.get_title(url)
            
        except Exception as e:
            print e
    elif komut == "brute":
        try:
            wp_brute.run()
        except:
            print red + "An error... Try again later"
        
        
            
        
        
    
        
