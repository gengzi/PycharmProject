# -*- coding: UTF-8 -*-

# 导入urllib2的类库
import  urllib2
# User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36

ua_header ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"}

# 打开一个链接
urlstr = "http://www.baidu.com/"   #这个 / 是需要写的
# 返回一个类文件
request = urllib2.Request(urlstr,headers=ua_header)
response = urllib2.urlopen(request)

# 获取相应结果
html = response.read()

print(html)

