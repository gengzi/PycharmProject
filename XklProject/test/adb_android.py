#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习

# 添加更多的Header信息
# 构造一个完成的url请求


import os
import time


def load():
    # os.system("adb shell input swipe 1000 1000 1 1")
    os.system("adb shell input swipe 500 500 3 3")
    time.sleep(1)



if __name__ =="__main__":
    for i in range(1,10000):
        print("第"+str(i)+"次")
        load()
