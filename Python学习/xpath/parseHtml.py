#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习

from lxml import etree

html = """
<html>
    <head>
        <base href='http://example.com/' />
        <title>Example website</title>
    </head>
    <body>
        <div id='images'>
            <a href='image1.html'>Name: My image 1 <br/><img src='image1_thumb.jpg'/></a>
            <a href='image2.html'>Name: My image 2 <br/><img src='image2_thumb.jpg'/></a>
            <a href='image3.html'>Name: My image 3 <br/><img src='image3_thumb.jpg'/></a>
            <a href='image4.html'>Name: My image 4 <br/><img src='image4_thumb.jpg'/></a>
            <a>Name: My image 5 <br/><img src='image5_thumb.jpg'/></a>
        </div>
    </body>
</html>
"""
page_source =etree.HTML(html.decode("UTF-8"))



title = page_source.xpath("//title/text()")
all_href = page_source.xpath("//a/@href")
a_image1_text = page_source.xpath("//body//a[1]/text()")
a_image1_src = page_source.xpath("//a[@href='image1.html']/img/@src")
a_image3_href = page_source.xpath("//a[contains(@href, '3')]/@href")
a_last = page_source.xpath("//body//a[last()]/img/@src")
all_img_src = page_source.xpath("//img/@src")

print "Title", title
print "all href", all_href
print "a_image1_text", a_image1_text
print "a_image1_src", a_image1_src
print 'a_image3_href', a_image3_href
print "a_last", a_last
print "all_img_src", all_img_src











