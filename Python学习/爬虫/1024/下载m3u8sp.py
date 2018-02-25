                                                                                                                                                                                                                             #!/usr/bin/env python2
# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言
import re
import random
import requests
import uuid
import json
from Queue import Queue
import threading
import time
# 使用 lxml 的 etree 库
from lxml import etree
import os

"""
    单线程爬取视频  // 修改为多线程爬虫 // 使用代理
    author：gengzi
    version：0.0.1.3
    sj：2018年2月13日13:00:54
"""
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

if __name__ == "__main__":
    # os.system("ffmpeg -i http://videows1.douyucdn.cn/live/high_9420556220180209180944-upload-d43d/5bf97910a3b24f9fa6dcc31764bafee5_0000019.ts?k=e3852254edfb389a3c816a6f4712ad56&t=5a8676b2&u=2162233&ct=web&vid=2865545&d=B4AC01967561B7FDC8DCE3221A7B5126  H:\\python\\sp\\2.mp4")
    os.system("ffmpeg -i https://v.dyzy9.com/ppvod/n4xv9BMc.m3u8  H:\\python\\sp\\3.mp4")





