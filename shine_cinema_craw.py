#-*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import csv

shine_cinema='http://www.ygdy8.com'
user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
headers={'User-Agent':user_agent}   #设置请求头，无此设置时，在爬取至60页时，会禁止爬取
base_url='http://www.ygdy8.com/html/gndy/china/list_4_'     #在此基础上，对网页进行迭代
entry_url='http://www.ygdy8.com/html/gndy/china/index.html' #第一页网址比较特殊，独立出来进行爬取

# f=open('china-cinema.csv','a+',newline='',encoding='utf-8')
# csvWrite=csv.writer(f)

#请求网页
def download(url):
    r=requests.get(url,headers=headers)
    r.encoding='gb2312'     #处理中文显示乱码
    return r

#获取电影下载地址
def get_download_url(url):
    r=download(url)
    soup=BeautifulSoup(r.text,'lxml')
    download_url=soup.select('table tr > td > a')[0]['href']
    # print(type(download_url))
    return download_url

#获取电影相关信息
def get_ciname_url(url):
    soup = BeautifulSoup(url, 'lxml')
    link=soup.select('b > a:nth-of-type(2)')
    for i in range(len(link)):
        download_url=get_download_url(shine_cinema+link[i]['href'])
        print(link[i].text,'地址：'+shine_cinema+link[i]['href'],'下载地址：'+download_url)


def iter_url():
    for i in range(2,94):
        r=download(base_url+str(i)+'.html')
        print("这是第{}页".format(i))
        get_ciname_url(r.text)

index=download(entry_url)
get_ciname_url(index.text)
iter_url()
# Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36