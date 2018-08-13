import re
import urllib.request
def craw(url,page):
    html1=urllib.request.urlopen(url).read()
    html1=str(html1)
    #第一次过滤
    pat1='<div id="plist".+?<div class="page clearfix">'
    result1=re.compile(pat1).findall(html1)
    result1=result1[0]

    #第二次过滤
    pat2='<img width="220" height="220" data-img="1" src="//(.+?\.jpg)">'
    print(pat2)
    imagelist=re.compile(pat2).findall(result1)
    print(imagelist)
#    x=1
#    for imageurl in imagelist:
#        imagename='D:\crawtu\img'+str(page)+str(x)+'.jpg'
#        imageurl='http://'+imageurl
#        try:
#            urllib.request.urlretrieve(imageurl,filename=imagename)
#        except urllib.error.URLError as e :
#            if hasattr(e,'code'):
#                x+=1
#            if hasattr(e,'reason'):
#                x+=1
#        x+=1
        

#for i in range(1,10):
url='https://list.jd.com/list.html?cat=9987,653,655&page='+str(1)
craw(url,1)
