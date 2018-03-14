#!/usr/bin/env python2
# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习

import sys
reload(sys)
sys.setdefaultencoding('utf8')  #设置系统编码格式
import ConfigParser


# 读取配置文件
cf = ConfigParser.ConfigParser()
cf.read("Bmob.conf")
opts = cf.options("dbaname")


