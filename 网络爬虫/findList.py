import urllib.request
f = urllib.request.urlopen(r"http://www.baidu.com")
file = open("baidu.html",'w',encoding='utf8')
file.write(f.read().decode('utf8'))
#file.write(str(content))
f.close()
file.close()
