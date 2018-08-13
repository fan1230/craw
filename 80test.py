
import urllib.request
import re
def getcontent(url,page):
    #模拟成浏览器
    headers=('User-Agent','Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0')
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    #将opener安装为全局
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode("utf-8")
    #构建对应用户提取的正则表达式
    userpat='<h2>(.*?)</h2>'
    #段子内容正则
    contentpat='<div class="content">(.*?)</div>'
    #寻找所有用户
    userlist=re.compile(userpat,re.S).findall(data)
    #寻找出所有内容
    contentlist=re.compile(contentpat,re.S).findall(data)
    x=1
    #遍历内容
    for content in contentlist:
        content=content.replace('\n','')
        name='content'+str(x)
        exec(name+'=content')
        x+=1
    y=1
    #遍历用户
    for user in userlist:
        name='content'+str(y)
        print('用户'+str(page)+str(y)+'是:'+user)
        print('内容是:')
        try:
            exec("print("+name+")")
        except:
            import time
            time.sleep(0.1)
        print('\n')
        y+=1


#启动
for i in range(1,13):
    url='https://www.qiushibaike.com/8hr/page/'+str(i)
    getcontent(url,i)
