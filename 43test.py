import urllib.request
import urllib.parse
url='http://www.guitarworld.com.cn/member.php?mod=logging&action=login&referer=&formhash=50596a66'
postdata=urllib.parse.urlencode({
    'phone':'fan123',
    'password':'buy5230'
    }).encode('utf-8')

req=urllib.request.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0')
data=urllib.request.urlopen(req).read()
fh=open(r'C:\Users\fan\Desktop\spider_test\43test.html','wb')
fh.write(data)
fh.close()
