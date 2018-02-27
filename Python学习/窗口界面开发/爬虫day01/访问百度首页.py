# -*- coding: UTF-8 -*-

# 导入urllib2的类库
import  urllib2

# 打开一个链接
urlstr = "http://www.baidu.com/"
# 返回一个类文件
response = urllib2.urlopen(urlstr)

# 获取相应结果
html = response.read()

print(html)

