#coding:utf-8

import urllib
import sys
from bs4 import BeautifulSoup

class GetWebContent():
    def __init__(self, url):
        self.url = url
        self.stationList = []

    def getContent(self):
        result = []
        page = urllib.urlopen(self.url)#打开网页
        htmlcode = page.read()#读取页面源码
        soup = BeautifulSoup(htmlcode, "lxml")
        #print soup.select('.page-content')
        a = soup.find("div", class_='portlet-body')
        b = a.findAll(attrs={"class": "btn grey"})
        #b = a.select(".btn grey")
        for ab in b:
            print ab.get_text()
            result.append(self.url[:-6]+ab.get("href"))
        #print a
        return result
    def getStationName(self, url):
        page = urllib.urlopen(url)  # 打开网页
        htmlcode = page.read()  # 读取页面源码
        soup = BeautifulSoup(htmlcode, "lxml")
        a = soup.findAll(attrs={"class": "portlet-body"})
        for aa in a:
            b = aa.find_all('a')
            for bb in b:
                c = bb.get_text()
                c = c.strip()
                if c not in self.stationList:
                    self.stationList.append(c)
                    print c
                #print b
        #print a

    def getCityName(self, url):
        result = []
        page = urllib.urlopen(url)  # 打开网页
        htmlcode = page.read()  # 读取页面源码
        soup = BeautifulSoup(htmlcode, "lxml")
        a = soup.findAll(attrs={"class": "portlet-body"})
        b = a[1]
        #print b
        c = b.find_all('a')
        for cc in c:
            d = self.url[:-6]+cc.get('href')
            result.append(d)
        return result
    def getnum(self):
        return self.stationList


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding("utf-8")
    fo = open("foo.txt", "w")
    se = GetWebContent('http://www.qichezhan.net/city/')
    result = se.getContent()
    print result
    n = 0
    for ree in result:
        n +=1
        se.getStationName(ree)
        if n<=4:
            se.getStationName(ree)
        else:
            trww = se.getCityName(ree)
            for it in trww:
                se.getStationName(it)
    #print se.getnum()
    #print se.getCityName('http://www.qichezhan.net/zj/')
    for it in se.getnum():
        fo.write(it)
        fo.write('\n')

    # 关闭打开的文件
    fo.close()