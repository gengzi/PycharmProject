#!/usr/local/bin/python
#coding=utf-8

import logging
import logging.handlers
import sys
reload(sys)
sys.setdefaultencoding('utf8')  #设置系统编码格式
from wechat_sender import *
# log 文件日志
LOGFILE = "H:\\python\\xiakeliao\\xkl.log"
# 实例化Handler
handler = logging.handlers.RotatingFileHandler(filename=LOGFILE,maxBytes=1024*1024,backupCount=2)
# 日志的输出格式
fm = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
format =logging.Formatter(fm)
handler.setFormatter(format)

# 控制台打印日志
handler_console = logging.StreamHandler(sys.stdout)
handler_console.setFormatter(format)

# 将日志发送到微信端
sender_logger = LoggingSenderHandler(level=logging.ERROR)



logger = logging.getLogger("xkl")
# 设置在文件中写log
# 设置Handler,在文件中
logger.addHandler(handler)
# 设置在控制台写log
logger.addHandler(handler_console)
# 设置在微信端
# logger.addHandler(sender_logger)
# 设置日志级别
logger.setLevel(logging.DEBUG)


# 测试
# logger.info('first info message')
# logger.debug('first debug message')






