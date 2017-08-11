import csv
import requests
from bs4 import BeautifulSoup
import time
from requests.exceptions import RequestException
from multiprocessing.dummy import Pool as ThreadPool
import pandas as pd

simple_book = 'http://www.jianshu.com'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
headers = {'User-Agent': user_agent}
base_url = 'http://www.jianshu.com/recommendations/users?page='  # 推荐作者页面在此基础上进行迭代
recommend_author = {}


# UserName=set()

# def write_to_csv(name,url,follow_num,fans_num,article_num,word_num,get_like):
#     csvWrite.writerow([name,url,follow_num,fans_num,article_num,word_num,get_like])
# jishu=0
def download(url):
    try:
        r = requests.get(url, headers=headers)
        return r
    except RequestException as e:
        print("The problem is {}".format(e))


# http://www.jianshu.com/users/3aa040bf0610/followers?page=2
followStr = '/followers?page='
# num=0
def get_User_info(url):
    # i=0
    try:
        r = requests.get(url, headers=headers)

        soup=BeautifulSoup(r.text,'lxml')
        user_list=soup.find_all('div',class_='info')
        for i in range(len(user_list)):
            name=user_list[i].find('a',class_='name')
            if name == None:
                continue
            else:
                follow_fan_article=user_list[i].find_all('div',class_='meta')   #这个div下包括了关注人数，粉丝数，文章数
                follow = follow_fan_article[0].select('span:nth-of-type(1)')[0].text.strip()
                # print(follow)
                fan = follow_fan_article[0].select('span:nth-of-type(2)')[0].text.strip()
                article = follow_fan_article[0].select('span:nth-of-type(2)')[0].text.strip()
                word=follow_fan_article[1].text.strip().replace('\n','')
                not_recommend_csvWrite.writerow([name.text,follow,fan,article,word])

    except RequestException as e:   #异常处理
        print("The problem is {}".format(e))
def get_not_recommend_author_info(url, name,fan_num):
    # index = 1
    fan_num=int(fan_num)

    UserUrlList=[]
    if(fan_num%9 == 0):max_index=fan_num//9
    else:max_index=fan_num//9+1
    print("{}下请求的用户页面!".format(name))
    print(name,url,'粉丝数:',fan_num)

    for index in range(1,101):  #理论上来说此处将范围设置为(1,max_index)，应该是可以抓取所有粉丝
        UserUrlList.append(url + followStr + str(index))
        index+=1

        # print(url + followStr + str(index))
    pool.map(get_User_info,UserUrlList)     #将所获得的粉丝请求页面传入所开启的线程池

def get_recommend_author_info():

    page_index = 1
    while True:
        r = download(base_url + str(page_index))
        print("第{}个请求页面！".format(page_index))
        soup = BeautifulSoup(r.text, 'lxml')
        stop_mark = soup.find('div', class_='col-xs-8')  # 通过定位页面中的这个元素来停止页面的请求
        if stop_mark:  # 如果存在该元素，则进行推荐作者相关信息的获取
            author_name = soup.find_all('h4', class_='name')  # 获取作者姓名

            author_url = soup.select('div[class~=wrap] > a')  # 获取推荐作者链接。此处通过css3来定位标签
            for i in range(len(author_url)):
                # recommend_author[author_name[i].text.strip()]=simple_book+author_url[i]['href'].strip()
                authorHtml=download(simple_book+author_url[i]['href'].strip())
                authorSoup=BeautifulSoup(authorHtml.text,'lxml')
                recommend_author_info=authorSoup.select('div[class~=info] > ul > li')   #返回的列表中包含了推荐作者的一些信息
                name=author_name[i].text.strip()

                url=simple_book+author_url[i]['href'].strip()   #推荐作者首页链接
                follow_num=recommend_author_info[0].select('p')[0].text     #关注人数
                fans_num=recommend_author_info[1].select('p')[0].text       #粉丝人数

                article_num = recommend_author_info[2].select('p')[0].text      #文章数
                word_num = recommend_author_info[3].select('p')[0].text     #字数
                getLike_num = recommend_author_info[4].select('p')[0].text      #获得喜欢数

                # recommend_csvWrite.writerow([name,url,follow_num,fans_num,article_num,word_num,getLike_num])  #将推荐作者的相关信息写入csv文件
                get_not_recommend_author_info(url,name,fans_num)
            page_index += 1
            # time.sleep(1)
        else:
            break  # 当请求的页面无该元素时，则说明本页面不存在推荐作者，跳出循环
def quchong():
    csvfile = 'GetUser.csv'
    file = pd.read_csv(csvfile, header=0)
    dateList = file.drop_duplicates()
    dateList.to_csv(csvfile)

start = time.time() #记录程序开始时间
pool = ThreadPool(4)
#推荐作者的csv文件
recommendFile = open('recommend_author.csv', 'a+', newline='', encoding='utf-8')
recommend_csvWrite = csv.writer(recommendFile)
recommend_csvWrite.writerow(['作者名', '首页链接', '关注人数', '粉丝', '文章', '字数', '收获喜欢'])

#所获取到的用户csv文件
notRecommendFile = open('GetUser.csv', 'a+', newline='', encoding='utf-8')
not_recommend_csvWrite = csv.writer(notRecommendFile)
not_recommend_csvWrite.writerow(['用户名', '关注数', '粉丝数', '文章数'])

get_recommend_author_info()
quchong()
pool.join()

#


end = time.time()   #记录结束时间
# print(UserName)
print("总耗时 %0.2f分钟！" % ((end - start)/60))
#
