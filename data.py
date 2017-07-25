#coding:utf8
import urllib
import urllib2
import re,random

def FindPat(pat,source):
    rr=re.compile(pat)
    namelist=re.findall(rr,source)
    return namelist


def GetPage(url,data,ip_pool,agents_pool):
    if(ip_pool!=[] and random.randint(0,1)!=0):
        proxy={'http':'%s'%random.choice(ip_pool)}
        proxy_support = urllib2.ProxyHandler(proxy)
        opener = urllib2.build_opener(proxy_support)
        urllib2.install_opener(opener)
    headers = {'User-Agent': '%s'%random.choice(agents_pool)}
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    page = response.read()
    return page

def DownLoad(url,data,path,sig):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    page = response.read()
    with open(path,sig) as file:
        file.write(page)

def DownLoad_Proxy(url,data,path,sig):
    proxy={'http':'127.0.0.1:8087'}
    proxy_support = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    page = response.read()
    with open(path,sig) as file:
        file.write(page)
