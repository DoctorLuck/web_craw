import requests
from bs4 import BeautifulSoup
import re

user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
headers={'User-Agent':user_agent}
# base_url='http://www.jianshu.com/c/1b31f26b6af0?order_by=added_at&page='
base_url='http://www.jianshu.com/c/5AUzod?order_by=added_at&page='

authorList={}

def download(url):
    r=requests.get(url,headers=headers)
    return r
def get_article_num(url):   #获取文章总数
    r = download(url)
    soup = BeautifulSoup(r.text, 'lxml')
    special_topic_info = soup.find('div', class_='info').text.strip()  #
    article_num = int(re.search(r'\d+', special_topic_info).group())
    return article_num
def run():
    page_index = 1
    num=0
    while num<=article_num:
        print("第{}页作者...".format(page_index))
        r=download(base_url + str(page_index))
        soup=BeautifulSoup(r.text,'lxml')
        author=soup.find_all('a',class_='blue-link')
        article=soup.find_all('li',id=re.compile(r'\d+'))
        for i in range(len(author)):
            if(author[i].text not in authorList):
                authorList[author[i].text]=1
            else:
                authorList[author[i].text] = 1+authorList[author[i].text]
        if len(author) == 0: break
        print(len(author))
        num += len(author)
        page_index += 1

    for k, v in authorList.items():
        print(k + 5 * '  ' + str(v))
article_num=get_article_num(base_url + str(1))
run()



