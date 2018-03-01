# -*- coding:utf-8 -*-

import time
import os
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')

"""
    时间操作常用方法
    author：gengzi
    version：0.0.1
    sj：2018年3月1日16:45:00
"""

def getNewFormatTime(formatStr):
    """
    返回当前格式后的时间
    :param:formatStr 时间的格式 str
    :return:
    """
    return time.strftime(formatStr,time.localtime(time.time()))


def getTimeStamp(formateTime):
    """
    获取当前时间的时间戳 10 位
    :param formateTime 格式好的时间  %Y-%m-%d %H:%M:%S
    :return: int类型的时间戳
    """
    return int(time.mktime(time.strptime(formateTime, "%Y-%m-%d %H:%M:%S")))

def getYesterday(formatStr):
    """
     获取昨天的日期
    :param formatStr: 时间格式
    :return: 年-月-日
    """
    return (datetime.datetime.now() - datetime.timedelta(days=1)).strftime(formatStr)


def getFormatTimeByTimestamp(formatStr,timestamp):
    """
    根据时间戳返回格式化的当前时间
    :param:timestamp 时间戳
    :param:formatStr 格式时间
    :return: 格式好的时间
    """
    return time.strftime(formatStr,time.localtime(float(timestamp[0:10])))
