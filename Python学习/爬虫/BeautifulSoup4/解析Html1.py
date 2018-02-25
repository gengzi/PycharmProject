#!/usr/bin/env python2
# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言

from bs4 import BeautifulSoup
import json
# 使用 lxml 的 etree 库
from lxml import etree


# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
#
# soup = BeautifulSoup(html,"lxml")
#
# print(soup.prettify())


str = '< div id = "a1" class ="video-container" style="width:100%; height:530px;;" > < script > var VideoInfoList="mp4$$mp4$http://api2.hitimg.info:8880/j.php?y=/get_file/3/fc908fab3ba534b7f883fe54a5c9a919/80000/80576/80576.mp4/$mp4" < / script > < script > var paras=getAspParas(".html);_lOlOl10l(paras[2], paras[1]) < / script > < iframe id="cciframe" scrolling="no" frameborder="0" allowfullscreen > < / iframe > < / div >';

doc=etree.HTML(str);
video_a = doc.xpath('//div[@class="video-container"]//')
print(video_a)