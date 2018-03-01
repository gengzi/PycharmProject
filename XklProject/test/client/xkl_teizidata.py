# -*- coding:utf-8 -*-
from wechat_sender import Sender
import requests
import time
import json
import os
import jsonpath
import datetime
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf8')
"""
    author：gengzi
    version：0.0.1.3
    sj：2018年2月27日23:43:35
"""
headers = {"User-Agent": 'okhttp/3.6.0'}
posturl = "http://120.55.151.61/V2/Treehole/Message/getMessageByTopicIdV5.action"
def postStudent(session,beforTimestamp,afterTimestamp,topicId):
    print("开始的时间戳:"+beforTimestamp)
    print("结束的时间戳:"+afterTimestamp)
    post_url= "http://120.55.151.61/V2/Treehole/Message/getMessageByTopicIdV5.action"
    #请求的数据
    postdata = {
        "channel":"XiaoMiMarket",
        "genderType":"-1",
        "phoneBrand":"Xiaomi",
        "phoneModel":"HM 2A",
        "phoneVersion":"19",
        "platform":"1",
        "selectType":"0",
        "timestamp":afterTimestamp,
        "topicId":topicId,
        "type":"1",
        "versionNumber":"9.3.1",
    }

    student_response = session.post(url=post_url,headers=headers,data=postdata)
    timestamp = paseJsondata2Timestamp(student_response.text)
    # 年月日，时分秒
    formatTime = getFormatTimeByTimestamp("%Y-%m-%d %H:%M:%S", timestamp)
    # 年月日
    formatTimeday = getFormatTimeByTimestamp("%Y-%m-%d", timestamp)
    print("该分页数据的时间：" + formatTime)
    print("栏目编号：" + topicId)
    print("时间戳：" + timestamp)
    print("整个数据的日期：" +formatTimeday)
    # 目录
    yesterday = getYesterday("%Y-%m-%d")
    # 创建目录
    path = "/home/ubuntu/python_workspace/xiakeliao/tiezidata/" + yesterday + "/"
    insertData(path+timestamp+".txt",formatTime,topicId,timestamp,formatTimeday)
    # 休眠10秒，模拟人工操作
    time.sleep(15)
    if int(timestamp) >= int(beforTimestamp):
        postStudent(session,beforTimestamp,timestamp,topicId)
    else:
        return

def paseJsondata2Timestamp(response):
    """
    解析出timestamp
    :param response: 响应的数据
    :return: timestamp
    """
    # 将响应数据写入txt文件
    jsondata = json.loads(response)
    # 解析出来下一次分页的时间戳
    timestampList = jsonpath.jsonpath(jsondata, "$.data.timestampLong")
    #文件名为时间戳.txt
    timestamp = str(timestampList[0])
    filename = timestamp+".txt"
    #目录
    yesterday = getYesterday("%Y-%m-%d")
    # 创建目录
    path = "/home/ubuntu/python_workspace/xiakeliao/tiezidata/"+yesterday+"/"
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        os.makedirs(path)
        print path + '创建成功'
    filepath = path+filename
    #先写入文件
    with open(filepath, "w") as code:
        code.write(response)
    return timestamp

def login():
    """
    登陆，返回登陆成功的session
    :return:  session
    """
    try:
        url_login = "http://120.55.151.61/V2/StudentSkip/loginCheckV4.action"
        # 密码和账号都是加密后的
        login_data = {
            "account": "F5169A5DCC50A9DE4EB747493BCD3BCB",
            "channel": "XiaoMiMarket",
            "deviceCode": "868291022946681",
            "password": "07912E33F75EAF6172814A17E2EE0059",
            "phoneBrand": "Xiaomi",
            "phoneModel": "HM 2A",
            "phoneVersion": "19",
            "platform": "1",
            "updateInfo": "false",
            "versionNumber": "9.3.1",
        }
        # 模拟登陆
        session = requests.session()
        session.post(url=url_login, headers=headers, data=login_data)
        # session会携带登陆后的cookie回来
        return session
    except Exception,e:
        print(e)
        print("登陆失败")

def insertData(response,formatTime,topicId,timestamp,formatTimeday):
    """
    将数据写入数据库
    :param response: 响应的json数据
    :param formatTime: 年月日时分秒
    :param topicId: 栏目的编号
    :param timestamp: 时间戳
    :param formatTimeday: 年月日
    :return: 是否成功
    """
    try:
        conn = MySQLdb.connect(host="123.206.30.117",port=3306,user="root",passwd="111",db="xklinfo",charset="utf8")
        cursor =conn.cursor()
        # 封装参数
        # 将响应数据中的 unicode
        params = [str(formatTimeday),response,str(timestamp),str(formatTime),str(topicId)]
        #插入
        sql ="insert into messagedata(nowtime,datajson,timestamp,stampdate,topicid) values(%s,%s,%s,%s,%s)"
        count = cursor.execute(sql, params)
        if count >= 1:
            print("成功")
        conn.commit()
    except Exception,e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def getFormatTimeByTimestamp(formatStr,timestamp):
    """
    根据时间戳返回格式化的当前时间
    :param:timestamp 时间戳
    :param:formatStr 格式时间
    :return: 格式好的时间
    """
    return time.strftime(formatStr,time.localtime(float(timestamp[0:10])))

def getYesterday(formatStr):
    """
     获取昨天的日期
    :param formatStr: 时间格式
    :return: 年-月-日
    """
    return (datetime.datetime.now() - datetime.timedelta(days=1)).strftime(formatStr)

def getTimeStamp(formateTime):
    """
    获取当前时间的时间戳
    :param formateTime 格式好的时间  %Y-%m-%d %H:%M:%S
    :return: int类型的时间戳
    """
    return int(time.mktime(time.strptime(formateTime, "%Y-%m-%d %H:%M:%S")))

def gettopicIds():
    """
    获取需要抓取的栏目的id
    :return:
    """
    return (19,13,38,41,15)

def getNewFormatTime():
    """
    返回当前格式后的时间
    :return:
    """
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

if __name__ == "__main__":
    send = Sender()

    # [1]拿到登陆成功的session
    session = login()
    send.delay_send(content="爬取帖子，抽取数据开始",title="下课聊",time=getNewFormatTime())
    # [2] 抓取昨天发布的全部帖子，一些小的栏目帖子不算
    # 获取上一天的年月日
    yesterday = getYesterday("%Y-%m-%d")
    print yesterday
    # 模拟抓取的时间戳
    # 0.0.0 的时间戳  23.59.59 的时间戳
    befor_timestamp = str(yesterday)+" 00:00:00"
    after_timestamp = str(yesterday)+" 23:59:59"
    print befor_timestamp
    beforTimestamp = getTimeStamp(befor_timestamp)
    afterTimestamp = getTimeStamp(after_timestamp)
    # 组拼成13位的时间戳
    beforTimestamp = str(beforTimestamp)+"000"
    afterTimestamp = str(afterTimestamp)+"999"
    # 调用请求数据方法
    print(str(yesterday)+"抽取数据开始>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    # [2.1] 将五个模块的数据都抓取出来
    topicIds = gettopicIds()
    for i in topicIds:
        try:
            print("爬取的栏目编号:"+str(i))
            send.delay_send(content="爬取的栏目编号"+str(i),title="下课聊",time=getNewFormatTime())
            postStudent(session,beforTimestamp,afterTimestamp,str(i))
        except Exception,e:
            print(e)
            print("栏目编号:"+str(i)+"爬取出错")
            send.delay_send(content="爬取的栏目编号"+str(i)+"出错",title="下课聊",time=getNewFormatTime())
            continue
    print(str(yesterday)+"抽取数据结束>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    send.delay_send(content=str(yesterday)+"抽取数据结束>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",time=getNewFormatTime())



