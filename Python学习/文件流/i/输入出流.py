# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言”

# 文件写入 w wb
f = open(r"E:\python_file\py.txt",'a')
f.write('gengzi')
f.flush()
f = open(r"E:\python_file\py.txt",'r')
print(f.read())
f.close()


