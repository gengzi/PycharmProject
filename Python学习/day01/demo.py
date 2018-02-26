# coding=utf-8
import webbrowser
import time
import urllib2
import re
import os
import thread

tabcount = 1


def BlogFun(n, url, MaxVisitor):
    visitcount = r'<span class="link_view" title="阅读次数">(\d+)人阅读</span>'
    global tabcount
    while True:
        if tabcount > 10:
            os.system('taskkill /F /IM chrome.exe')
            tabcount = 1
        else:
            tabcount = tabcount + 1
        webbrowser.open(url, new=1)
        request = urllib2.Request(url)
        request.add_header('User-Agent',
                           'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')
        opener = urllib2.build_opener()
        fblog = opener.open(request)
        htm = fblog.read()
        Ref = re.findall(visitcount, htm);
        print url + ": " + str(int(Ref[0])) + "人阅读"
        if int(Ref[0]) > MaxVisitor:
            break
        time.sleep(n)


if __name__ == "__main__":
    Domain = "http://blog.csdn.net"
    Blog_url = "http://blog.csdn.net/qq_28817739/article/details/78941378"
    FreshSecond = 3
    MaxVisitor = 1000
    BlogFun(FreshSecond, Blog_url, MaxVisitor)