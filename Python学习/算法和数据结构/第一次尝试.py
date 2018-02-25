#!/usr/bin/env python2
# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言


# import time
#
#
# start_time = time.time()
#
# # 注意是三重循环
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a**2 + b**2 == c**2 and a+b+c == 1000:
#                 print("a, b, c: %d, %d, %d" % (a, b, c))
#
#
# end_time = time.time()
# print("elapsed: %f" % (end_time - start_time))
# print("complete!")



import time

start_time = time.time()

# 注意是两重循环
for a in range(0, 1001):
    for b in range(0, 1001-a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a, b, c: %d, %d, %d" % (a, b, c))

end_time = time.time()
print("elapsed: %f" % (end_time - start_time))
print("complete!")