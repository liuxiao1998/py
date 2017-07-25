#coding:utf8
import data,os,time
with open('./user_agents.txt','r') as uf:
    agents_pool=[]
    for lines in uf:
        if(lines!='\n'):
            agents_pool+=lines
with open('./ip.txt','r') as fp:
    ip_pool=[]
    for sd in fp:
        ip_pool+=fp

res=data.GetPage('http://www.biquzi.com/0_213/',None,ip_pool,agents_pool)
name_pat=r'.html">(.*?)</a></dd>'
link_pat=r'<dd><a href="(.*?)">'
content_pat=r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />'
title_pat=r'<meta property="og:title" content="(.*?)"'
namelist=data.FindPat(name_pat,res)
linklist=data.FindPat(link_pat,res)
titlelist=data.FindPat(title_pat,res)
title=titlelist[0].decode('gb2312','ignore').encode('utf8','ignore')
print len(namelist),len(linklist)
k=0
os.system('mkdir ./%s'%title)

with open('./%s/%s.txt'%(title,title),'w') as fp:
    fp.write('%s\n'%title)
    sec=False
    for name in namelist:
        try:
            if(sec==False):
                fp.write('%s\n'%namelist[k].decode('gb2312','ignore').encode('utf8','ignore'))
            url='http://www.biquzi.com%s'%linklist[k].decode('gb2312','ignore').encode('utf8','ignore')
            page=data.GetPage(url,None,ip_pool,agents_pool)
            conlist=data.FindPat(content_pat,page)
            for lines in conlist:
                fp.write('    %s\n'%lines.decode('gb2312','ignore').encode('utf8','ignore'))
            sec=False
        except Exception as e:
            print e
            k-=1
            sec=True
        k+=1
        print '第%d章结束'%(k)
        fp.write('\n\n\n\n')
