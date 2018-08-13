import re
import urllib.request
import time
import urllib.error

#模拟浏览器
headers=('User-Agent','Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0')
opener=urllib.request.build_opener()
opener.addheaders=[headers]
#设为全局
urllib.request.install_opener(opener)
#设置一个列表listurl存储文章网址列表
listurl=[]
print(type(listurl))
#自定义函数,代理服务器
def use_proxy(proxy_addr,url):
    #建立异常处理机制
    try:
        import urllib.request
        proxy=urllib.request.ProxyHandler({'http':proxy_addr})
        opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data=urllib.request.urlopen(url).read().decode('utf-8')
        return data
    except urllib.error.URLError as e :
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
        #url异常延时10秒
        time.sleep(10)

    except Exception as e:
        print('Exception'+str(e))
        time.sleep(1)

#获取文章链接
def getlisturl(key,pagestart,pageend,proxy):
    try:
        page=pagestart
        #编码关键词key
        keycode=urllib.request.quote(key)
        pagecode=urllib.request.quote('page')

        #循环爬取链接
        for page in range(pagestart,pageend+1):
            #构建url
            url='https://weixin.sogou.com/weixin?query='+keycode+'&type=2'+'&page='+pagecode
            #url='https://weixin.sogou.com/weixin?type=2&query='+keycode+pagecode+str(page)
            #用代理服务器查询,解决ip封杀问题
            data1=use_proxy(proxy,url)
            #获取文章正则
            listurlpat='<div class="txt-box">.*?(http://.*?)"'
            #添加到列表listurl中
            listurl.append(re.compile(listurlpat,re.S).findall(data1))
        print('共获取到'+str(len(listurl))+'页')

        return listurl
    
    except urllib.error.URLError as e :
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
        #url异常延时10秒
        time.sleep(10)

    except Exception as e:
        time.sleep(1)

#通过文章链接获取对应内容
def getcontent(listurl,proxy):
    i=0
    fh=open(r'C:\Users\fan\Desktop\spider_test\87test.txt','wb')
    
    for i in range(0,len(listurl)):
        for j in range(0,len(listurl[i])):
            try:
                url=listurl[i][j]#取出一条url
                #处理成真实的url
                url=url.replace('amp;','')
                #使用代理去爬取对应的内容
                data=use_proxy(proxy,url)
                #文章标题正则
                titlepat='<h2 id="activity-name" class="rich_media_title">(.*?)</h2>'
                #文章内容正则
                contentpat='id="js_content">(.*?)id="js_sg_bar"'
                #通过正则匹配内容
                title=re.compile(titlepat).findall(data)
                content=re.compile(contentpat,re.S).findall(data)

                #初始化标题与内容
                thistitle='此次没有获取到'
                thiscontent='此次没有获取到'

                if (title!=[]):
                    thistitle=title[0]
                if (content!=[]):
                    thiscontent=content[0]
                #汇总
                dataall='<p>标题为:'+thistitle+'</p>''<p>内容为:'+thiscontent+'</p><br>'
                #写入文件
                fh.write(dataall.encode('utf-8'))
                print('第'+str(i)+'个网页第'+str(j)+'次处理')
                
            except urllib.error.URLError as e :
                if hasattr(e,'code'):
                    print(e.code)
                if hasattr(e,'reason'):
                    print(e.reason)
                #url异常延时10秒
                time.sleep(10)

            except Exception as e:
                print('exception:'+str(e))
                time.sleep(1)

    fh.close()

#入口
key='物联网'
proxy='127.0.0.1:8888'
pagestart=1
pageend=2
listurl=getlisturl(key,pagestart,pageend,proxy)
getcontent(listurl,proxy)

            
                
            




            
