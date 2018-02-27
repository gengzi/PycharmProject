# -*- coding: UTF-8 -*-
import  sys,os

#初始化工作只需在我们第一次导入模块时完成。
# Python 从 0 开始计数，而不是 1。
print('这一行的代码是：')
for i in sys.argv:
    print(i)

print(sys.path)
# 输出当前的工作空间
print(os.getcwd())