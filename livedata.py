import urllib.request
import csv
from bs4 import BeautifulSoup
from mechanize import Browser
from newspaper import Article
import stockstats
import datetime as datetime
import time
import random
def get_data(i):
    matrix[i]=[]
    url = "https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9"
    page = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    infile = urllib.request.urlopen(page).read()
    soup = BeautifulSoup(infile, 'lxml')
    flag = -50
    temp=[]
    for a in soup.find_all('td'):
        if (format(a.text).strip() != ""):
            if (format(a.text).strip()[-16:] == "Add to Portfolio"):
                temp=[]
                temp.append(format(a.text).strip()[:format(a.text).strip().find("\n")])
                #print(format(a.text).strip()[:format(a.text).strip().find("\n")])
                flag = 0
            if (flag == 4):
                temp.append(float(format(a.text).strip()))
                matrix[i].append(temp)
                flag += 1
            else:
                flag += 1
t1=time.time()
matrix=[None,None]
get_data(0)#first data
print("Company names:")
print("---------------")
for j in range(len(matrix[0])):
    print(matrix[0][j][0])
print("--------------------------------------Data will be displayed once every 1 minute. Please wait !")
while(True):#2 inutes interval getting data
    if(time.time()-t1>=10):
        t1=time.time()#initializing time for next 2 minutes
        get_data(1)#second data after 2 minutes
        for j in range(len(matrix[0])):
            if(abs(matrix[1][j][1]-matrix[0][j][1])>=0):
                print(matrix[0][j][0]+" => ",matrix[1][j][1])
        print("--------------------------------------Data will be displayed once every 1 minute. Please wait !")
        matrix[0]=matrix[1].copy()#copying second data to first
