import urllib.request
import csv
from bs4 import BeautifulSoup
from mechanize import Browser
from newspaper import Article
import requests
url= "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
infile=urllib.request.urlopen(page).read()
soup = BeautifulSoup(infile,'lxml')
section = soup.find("div", {"class": "fe4pJf"})
section1 = soup.find("div", {"class": "fe4pJf"})
s=""
maintitle= ""
mainurl=""
subtitle= ""
flag=0
z=0
k=0
time=[]
csv_file = open('google_news.csv', 'w')
writer = csv.writer(csv_file)
writer.writerow(["URL", "TIME", "MAIN-NEWS", "SUB-NEWS"])
for b in section1.find_all('time'):
    time.append(b["datetime"])
for a in section.find_all('a', href=True):
    ts=""
    for i in a['href'][2:]:
        if(i=='/'):
            break
        ts=ts+i
    if(ts == "publications"):
        continue
    elif (ts == "stories"):
        flag=0
        writer.writerow([mainurl, time[k], maintitle.replace("₹","Rs."), subtitle.replace("₹","Rs.")])
        print("url :\n",mainurl)
        print("time :\n",time[k])
        print("title :\n", maintitle)
        print("content :\n", subtitle, "\n\n")
        subtitle= ""
        k=k+z+1
        z=0
        continue
    s1="https://news.google.com/"+(a['href'][2:])
    if(s != s1 and format(a.text)!="" and (" " in format(a.text))):
        if(flag==0):
            maintitle=format(a.text)
            mainurl=s1
            flag=1
        elif(flag==1):
            z+=1
            subtitle+= format(a.text).strip() + "." + "\n "
        s=s1
csv_file.close()


