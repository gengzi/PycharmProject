# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言


import  os
import shutil
try:
    import cPickle as pickle
except ImportError:
    import pickle

print(os.getcwd()) # 获取python 脚本的工作路径


# 序列化和反序列化
# 序列化
d = dict(url="index.html",title="标题",content="首页")
print(d)
print(pickle.dumps(d))

f = open("E:\python_file\py.txt","a")
pickle.dump(d,f)
f.close()
# 反序列化
f = open("E:\python_file\py.txt","r")
d= pickle.load(f)    #engzigengzigengzigengzi(dp1
f.close()
