import requests
from bs4 import BeautifulSoup
import re

#爬取个人简书首页文章
articleList=[]  #用于保存所写的文章
articleInfo={}
jianshu='www.jianshu.com'
try:
    r=requests.get('http://www.jianshu.com/u/16d377e2ed69')     #获得了一个Response对象。更改入口时，修改此处链接
    print(r.url)
except Exception as e:
    print("The exception is {}".format(e))

soup=BeautifulSoup(r.text,'lxml')
# artList=soup.select('ul > li')  #获取ul下的直接子节点li
artList=soup.select('ul[class=note-list]')
# print(len(artList))   #判断出获取成功
# print(type(artList))
artList=artList[0]  #转换为Tag类型
# print(type(artList))  #观察类型
f=open('test.txt','a')
YM=re.compile(r'\d{4}-\d{2}-\d{2}')
HM=re.compile(r'\d\d:\d\d:\d\d')
lenTitle=[]
for article in artList.find_all('li'):
    title=article.find_all('a',class_='title')[0].text
    time=article.select('span[class=time]')[0]['data-shared-at']
    url=article.find_all('a',class_='title')[0]['href']
    getYM=re.search(YM,time)
    getHM=re.search(HM,time)
    finish_time=getYM.group()+'  '+getHM.group()
    lenTitle.append(len(title))
    print('标题: %30s  完成时间:%s  地址为： %s%s' % (title,finish_time,jianshu,url),file=f)





