import time
from datetime import datetime as dt

#Windows
#use as an administrator
#task scheduler -> create task with "Run with highest privileges" and with a proper "configure for"
#trigger -> at startup
#actions -> new -> "start a program" -> this app
#Linux/Mac hostsPath = r"/etc/hosts"
#open with sudo Cron -> @reboot python3 /path to this app

hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websiteList = ["www.facebook.com", "facebook.com"]
finalList = [redirect + " " + i for i in websiteList]
finalStringBlock = "\n".join(finalList)

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 15):
        print("Working time...")
        with open(hostsPath, 'r+') as file:
            content = file.read()
            for website in websiteList:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hostsPath, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websiteList):
                    file.write(line)
            file.truncate()
        time.sleep(2.5)