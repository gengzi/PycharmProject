#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习
from PIL import Image
import argparse


ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    img = u"I:\\2018-02-15all\\Friday_iOS-颖晨-8d4b0c00-11a2-11e8-b632-34e6d75e0715.jpg";

    im = Image.open(img)
    width = 80
    height = 80
    print im.format
    print im.size
    print im.mode



    im = im.resize((width,height), Image.NEAREST)

    txt = ""

    for i in range(width):
        for j in range(height):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print txt

    #字符画输出到文件
    with open("I:\\1.txt",'w') as f:
        f.write(txt)
