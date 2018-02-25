# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言
# import fork  linux 上面使用的

import os
import multiprocessing

# 子线程要执行的代码
def run_process(name):
    print("子进程{}({}) 正在运行 ".format(name,os.getpid()))

if __name__ =="__main__":
    print("父进程 {}".format(os.getpid()))
    for ipro in range(5):
        p = multiprocessing.Process(target=run_process,args=(str(ipro),))
        print("进程将要开启")
        p.start()  #启动进程
    p.join()  #实现进程间同步
    print("进程结束")
