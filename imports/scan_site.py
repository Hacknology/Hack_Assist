"""

            author: @Hacknology
            contact: utkucolak05@gmail.com
            date: 23.05.2017
"""

import requests
import time
import sys
import random
import re
import ragent


WPDork = [
    '("Just another WordPress site")', 
    '("Comment on Hello world!")', 
    '("Mr WordPress on Hello world!")', 
    '("uncategorized")', 
    '("author/admin")'
    ]
Site = "https://randomword.com"
WP_Dorks = []
SQL_Dorks = []
WP_Site = []
SQL_Site = []
links = []
page = 10

userAgent = {
    	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7'
        }
def create_word():
    #Black_Viking
    header = {'User-agent': ragent.ua()}
    req = requests.get(url=Site, headers=header, verify=False)
    word = re.findall('<div id="random_word">(.*?)</div>', req.text)[0]
    return word

def create_dork(num):
    '''WPFirst'''
    for i in range(1, int(num)+1):
        wp_dork = random.choice(WPDork) + create_word()
        WP_Dorks.append(wp_dork)
        return WP_Dorks
    
def wp_get_query(sayi):
    for i in range(len(WP_Dorks)):
        for s in WP_Dorks:
            say = 1
            while (say < sayi):
                requ = ('http://www.bing.com/search?q=' + s + '&first='+str(say))
                try:
                    r = requests.get(requ, verify=False)
                except Exception as e:
                    print "[-]Connection failed:" + e
                req = ''
                try:
                    link = re.findall('<h2><a href="(.+?)"', r.text)
                    for i in range(len(link)):
                        for i in range(len(link)):
                            if link[i].find('http://bs.yandex.ru'):
                                if link[i] not in links:
                                    links.append(link[i])
                                    print link[i]
                except: raise
