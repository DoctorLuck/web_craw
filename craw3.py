#coding : utf-8
import requests
from bs4 import BeautifulSoup
import re


base_url='http://www.jianshu.com/c/1b31f26b6af0?order_by=added_at&page='
argu=1      #修改网址
i=1     #统计总共的文章数，天知道怎么少知道，希望大佬告知
YM=re.compile(r'\d{4}-\d{2}-\d{2}')     #获得年月日的信息，此处通过span的属性获取
while True:
    r=requests.get(base_url+str(argu))
    soup=BeautifulSoup(r.text,'lxml')
    if argu>=14:
        break
    else:
        for article in soup.find_all('li',id=re.compile(r'note-\d{8}')):
            articleAuthor=article.find_all('a',class_='blue-link')[0].text
            articleTitle=article.find_all('a',class_='title')[0].text
            time=article.find_all('span',class_='time')[0]['data-shared-at']
            articleTime=re.search(YM,time).group()
            print(articleTitle+articleAuthor+articleTime)
            i+=1

        argu += 1
print(i)