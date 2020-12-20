from bs4 import BeautifulSoup
import re
import requests
from time import sleep
from os import system

while(1):
    url_t = "https://www.youtube.com/watch?v=pPmo21gkETU"
    url_s = "https://www.youtube.com/watch?v=KmIQ5sqr6NA"
    soup_t = requests.get(url_t).text
    soup_s = requests.get(url_s).text


    subs_t = re.findall(r"[0-9]\.[0-9][0-9]M subscribers", soup_t)[0]
    subs_s = re.findall(r"[0-9]\.[0-9][0-9]M subscribers", soup_s)[0]
    system("cls")
    
    realsubs_t = int(float(re.findall(r"[0-9]\.[0-9][0-9]", subs_t)[0])*100)
    realsubs_s = int(float(re.findall(r"[0-9]\.[0-9][0-9]", subs_s)[0])*100)
    
    if(realsubs_t > realsubs_s):
        print("TECHNO HAS MORE SUBS")
    elif(realsubs_t < realsubs_s):
        print("SKEPPY HAS MORE SUBS LOL")
    
    print("Skeppy (nerd) subs: "+subs_s+". Techno (never dies) subs: "+subs_t)
    
    
    sleep(0.01)