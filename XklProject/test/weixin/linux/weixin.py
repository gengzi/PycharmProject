#!/usr/bin/env Python
# coding=utf-8

from wxpy import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from wxpy import *
from wechat_sender import *
# 开启缓存验证
bot = Bot(cache_path="/home/ubuntu/python_workspace/xiakeliao/xkl/wx.png",console_qr=-2)
# 定时报告监听器状态
listen(bot=bot,status_report=True)
