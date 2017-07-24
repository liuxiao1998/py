#coding:utf8
import data
import os
js=10
zj=[96,93,187,195,187,90,95,96,96,190]
os.system("mkdir ./1")
for i in range(0,js,1):
    os.system("mkdir ./1/charpter%d"%(i+1))
    for k in range(0,zj[i],1):
        data.DownLoad("http://web2.cartoonmad.com/c86es736z62/1645/%03d/%03d.jpg"%(i+1,k+1),None,"./1/charpter%d/%d.jpg"%(i+1,k+1),"wb")
    print "%dfinished"%(i+1)
