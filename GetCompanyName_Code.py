# -*- coding: utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import time
import random

def getCity(url):
    result = []
    headers = {'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.8',
               'Cache-Control': 'max-age=0',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
               'Connection': 'keep-alive',
               'Referer': 'http://www.baidu.com/'
               }
    req = urllib2.Request(url, headers=headers)
    httpproxy_handler = urllib2.ProxyHandler({"http": "183.163.40.223:31773"})
    opener = urllib2.build_opener(httpproxy_handler)
    page = opener.open(req)
    #page = urllib2.urlopen(req)  # 打开网页
    htmlcode = page.read()  # 读取页面源码
    soup = BeautifulSoup(htmlcode, "lxml")
    #print soup.encode('utf-8')
    a = soup.find_all('div', id='filterArea')
    for aa in a:
        ab = aa.find_all('a')
        for ac in ab:
            result.append(ac['href'])
            print ac['href'], ac['title']
    return result

def getCompany(url):
    filename = 'fo.txt'
    with open(filename, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        httpproxy_handler = urllib2.ProxyHandler({"http": "183.163.40.223:31773"})
        opener = urllib2.build_opener(httpproxy_handler)
        page = opener.open(url + url_first)
        htmlcode = page.read()  # 读取页面源码
        soup = BeautifulSoup(htmlcode, "lxml")
        a = soup.find('div', class_='product_context')
        a = a.find_all('li', class_='product_box')
        for ss in a:
            a1 = ss.find('li', class_='pp_name')
            a1 = a1.a
            if not a1 == None:
                c = a1.get_text()
                f.write(c.encode('utf-8'))
                f.write('\n')
            a2 = ss.find('li', class_='c_name')
            if not a2 == None:
                d = a2.get_text()
                f.write(d.encode('utf-8'))
                f.write('\n')


def getAllcity(num):
    url = 'https://www.atobo.com.cn'
    urll = url + '/GongShang/s-p'+str(num)+'/'
    result_3 = []
    result_2 = getCity(urll)
    for item in result_2:
        ti = random.randint(0, 15)
        time.sleep(ti)
        print 'sleep'
        q = getCity(url + item)
        if not len(q):
            a = []
            a.append(item)
            result_3.append(a)
        else:
            result_3.append(q)
    '''for item in result_2:
        a = []
        a.append(item)
        result_3.append(a)'''
    filename = 'city'+str(num)+'.txt'
    with open(filename, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        for item in result_3:
            for it in item:
                f.write(it.encode('utf-8'))
                f.write('\n')


if __name__ == '__main__':
    '''url = 'https://www.atobo.com.cn'
    url_first = '/GongShang/'
    filename = 'city/city5.txt'
    result_list = []
    mylist = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            mylist.append(line.strip())
    for item in mylist:
        for index in range(51):
            if not index:
                continue
            res = item[:-1]+('-y'+str(index)+'/')
            result_list.append(res)
    print result_list
    for itr in result_list:
        real_url = url+itr
        print real_url
        ti = random.randint(0,15)
        time.sleep(ti)
        getCompany(real_url)

    '''
    '''
    result = []
    a = soup.find_all('div', class_='PD_ClassBlock')
    for aa in a:
        ab = aa.find_all('dt')
        for ac in ab:
            ad = ac.find_all('a')
            for ae in ad:
                result.append(ae['href'])
                print ae['href'], ae['title']
    '''
    '''
    urll = url+'/GongShang/s-p4/'
    result_3 = []
    result_2 = getCity(urll)
    for item in result_2:
        time.sleep(2)
        print 'sleep'
        q = getCity(url+item)
        if not len(q):
            a = []
            a.append(item)
            result_3.append(a)
        else:
            result_3.append(q)
    for item in result_2:
        a = []
        a.append(item)
        result_3.append(a)'''
    '''
    filename = 'city4.txt'
    with open(filename, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        for item in result_3:
            for it in item:
                f.write(it.encode('utf-8'))
                f.write('\n')
    '''
    index = 21
    while index < 30:
        ti = random.randint(0, 15)
        time.sleep(ti)
        getAllcity(index)
        index += 1










    '''for i in range(20):
        if i == 0:
            continue
            
        time.sleep(2)
        filename = 'fo'+str(i)+'.txt'
        getCompany('https://www.atobo.com.cn/GongShang/s-p5-s71-q64-y'+str(i)+'/')
        print i
    '''