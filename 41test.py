import urllib.request
url='https://www.baidu.com/s?wd='
key='韦玮老师'
key_code=urllib.request.quote(key)
url_all=url+key_code
req=urllib.request.Request(url_all)
data=urllib.request.urlopen(req).read()
fh=open(r"C:\Users\fan\Desktop\spider_test\41test.html","wb")
fh.write(data)
fh.close()
