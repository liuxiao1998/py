#coding:utf8

import data
def s(x):
    pat_title=r'class="j_th_tit ">(.*?)</a>'
    pat_author=r'主题作者: (.*?)\"'
    page=data.GetPage('http://tieba.baidu.com/f?kw=%E4%B8%8A%E6%B5%B7%E4%BA%A4%E9%80%9A%E5%A4%A7%E5%AD%A6&ie=utf-8&pn='+'%d'%x,None)
    title=data.FindPat(pat_title,page)
    author=data.FindPat(pat_author,page)
    k=0
    for i in title:
        try:
            print i.decode('utf8','ignore').encode('utf8','ignore'),'        by     ',author[k].decode('utf8','ignore').encode('utf8','ignore')
            k+=1
        except Exception,e:
            print Exception,':',e

for x in range(0,500,50):
    s(x)
