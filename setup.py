setup = raw_input("Setup ==> ")
if setup == "open valhalla's door":
    try:
        import pip
    except ImportError:
        import urllib2,sys,os
        source = urllib2.urlopen("https://bootstrap.pypa.io/get-pip.py").read()
        dosya = open("get-pip.py", "w").write(source)
        os.system(sys.executable + " get-pip.py")
    def yukle(module):
        pip.main(['install', module])
    try:
        import mechanize
        print "Mechanize imported!"
    except ImportError:
        yukle("mechanize")
    try:
        import colorama
        print "colorama imported!"
    except ImportError:
        yukle("colorama")
    try:
        import requests
        print "requests imported!"
    except ImportError:
        yukle("requests")
    try:
        import google
        print "google imported!"
    except ImportError:
        yukle("google")
    try:
        import ragent
        print "ragent imported!"
    except ImportError:
        yukle("ragent")
    print "[+] READY TO USE VALHALLA!"
