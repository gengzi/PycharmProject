# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言”


# 操作一个文件，可以使用 open() 方法将其打开
#  open(name[, mode[, buffering]]) -> file object
#   文件名字 ，可选参数 mode 模式，是那种模式 ，可选参数 是否使用缓存  -1 使用默认缓存
f = open("E:\python_file\py.txt","r",-1)
# f = open("E:\python_file\py.txt1","r",-1)  IOError: [Errno 2] No such file or directory: 'E:\\python_file\\py.txt1'
#  如果打不开，报异常
print(f.read())
#  关闭流
f.close()

# ------------------------------------------------

# 在出现文件读取不成功的时候，就会抛出异常。
# try:
#     f = open("E:\python_file\py.txt1","r",-1)
#     print(f.read())
# finally:
#     print("执行finally")
#     if f == None :
#         f.close()

# -------------------------------------------------


# -------------------------------------------------
#  python 提供了三种 读取的方式 。 read  read(size) readlines()

# read(size)
# size = 1024
# buff = []
# with open(r"E:\python_file\py.txt","r",-1) as fileReader:
#     for line in fileReader.read(size):
#         buff.append(line)
#     print(buff)

# readlines()
# with open(r"E:\python_file\py.txt","r",-1) as fileReader:
#     for line in fileReader.readlines():
#         print(line.strip())
# -------------------------------------------------








