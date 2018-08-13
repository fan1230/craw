import re
import urllib.request
import time
import urllib.error
listurl=[]

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

def getlisturl(key,pagestart,pageend,proxy):
    try:
        page=pagestart
        #编码关键词key
        keycode=urllib.request.quote(key)
        pagecode=urllib.request.quote(page)

        #循环爬取链接
        for page in range(pagestart,pageend+1):
            #构建url
            #url='https://weixin.sogou.com/weixin?query='+keycode+'&type=2'+'&page='+pagecode
            url='https://weixin.sogou.com/weixin?type=2&query='+keycode+pagecode+str(page)
            print(url)
            #用代理服务器查询,解决ip封杀问题
            data1=use_proxy(proxy,url)
            #获取文章正则
            listurlpat='<div class="txt-box">.*?(http://.*?)"'
            #添加到列表listurl中
            listurl.append(re.compile(listurlpat,re.S).findall(data1))
        print('共获取到'+str(len(listurl))+'页')

        print(listurl)
    except urllib.error.URLError as e :
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
        #url异常延时10秒
        time.sleep(10)

    except Exception as e:
        time.sleep(1)

key='物联网'
proxy='127.0.0.1:8888'
pagestart=1
pageend=5
getlisturl('物联网',1,5,'127.0.0.1:8888')
