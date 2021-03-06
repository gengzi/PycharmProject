#!/usr/local/bin/python
#coding=utf-8

import logging
import logging.handlers
import sys
# 创建 logging 记录器

# #简单的设置 logging 信息
# #设定日志的级别
# logging.basicConfig(level=logging.INFO)
# #几种日志的输入级别
# logging.debug("debug 信息")
# logging.info("info 信息")
# logging.warn("warning 信息")
# logging.error("error 信息")
# logging.critical("critical 信息")

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


logger = logging.getLogger("xkl")
# 设置在文件中写log
# 设置Handler,在文件中
logger.addHandler(handler)
# 设置在控制台写log
logger.addHandler(handler_console)
# 设置日志级别
logger.setLevel(logging.DEBUG)








logger.info('first info message')
logger.debug('first debug message')






