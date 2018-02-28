#!/usr/bin/env Python
# coding=utf-8

from wxpy import *
from wechat_sender import Sender
import  datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
"""
    登陆微信，持续监听
"""
send = Sender()
time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
send.delay_send(content="信息",title="标题",remind=datetime.timedelta(minutes=59),time=time)



