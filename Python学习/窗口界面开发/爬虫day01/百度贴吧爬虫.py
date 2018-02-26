# -*- coding: UTF-8 -*-


import  urllib2
import  urllib

"""
GET https://tieba.baidu.com/f?kw=90%E5%90%8E%E7%BE%8E%E5%A5%B3&pn=200 HTTP/1.1
Host: tieba.baidu.com
Connection: keep-alive
Cache-Control: max-age=0
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36
Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: BAIDUID=0C26D5DB0D5C18577C3A8AEDA900DF6E:FG=1; BIDUPSID=0C26D5DB0D5C18577C3A8AEDA900DF6E; PSTM=1514203968; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1439_21118_22157; PSINO=1; TIEBA_USERTYPE=ff4105377f994f87a1baa09e; bottleBubble=1; TIEBAUID=cb23caae14130a0d384a57f1; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1516113328,1516113340; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1516114633


"""



def loadPage(url):
    """
    作用：请求爬取的url
    :param url:
    :param filename:
    :return:
    """
    #构造请求
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"

    }
    request = urllib2.Request(url,headers=headers)
    #请求
    repsonse = urllib2.urlopen(request)
    return repsonse.read()



def wirteFile(html,filename):
    """
    作用：将html 的内容写入到 文件中
    :param html: 爬取的html页面
    :param filename:  文件名称
    :return:
    """
    with open(filename, 'w') as f:
        f.write(html)
    print "-" * 20




def teibaPC(url,startPage,endPage):
    """
    作用：组拼分页的url
    :param url: 爬取的路径
    :param startPage: 分页开始的页码
    :param endPage: 分页结束的页码
    :return:
    """
    #分析分页的特点
    for page in  range(start_page,end_page+1):
        pagenum = (page-1)*50
        #构造请求的url
        fyUrl =url+"&pn="+str(pagenum)
        print(fyUrl)
        #访问该url对应的网页数据
        filename = "D:\\pythonspce\\"+"90后美女吧-" + str(pagenum) + ".html"
        html = loadPage(fyUrl)
        #写入到本地文件中
        wirteFile(html,filename)




if __name__ == "__main__":
    teiba_name = raw_input("请输入爬取的百度贴吧名称：")
    start_page = int(input("请输入开始页码："))
    end_page = int(input("请输入结束页码："))

    kw = {"kw":teiba_name}
    url = "https://tieba.baidu.com/f?"+urllib.urlencode(kw)
    teibaPC(url,start_page,end_page)
