# -*- coding: utf-8 -*-
# 那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
#  下面是一个简单的高阶函数
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))

# map 函数 和 reduce函数
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

def f(x):
    return x*x

r = map(f,[1,23,33,44,33])
print(r)

# map()传入的第一个参数是f，即函数对象本身。

r1 = map(str,[1,1,3323,23,True,None])
print(r1)

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

from functools import  reduce

def qiuhe(x,y):
    return x+y
r3 = reduce(qiuhe,[1,2,3,4,5])
print(r3)
# 把序列[1, 3, 5, 7, 9]变换成整数13579
def fun01(x,y):
    return x*10+y;

r4 = reduce(fun01,[1,2,3,4,5])
print(r4)




def normalize(name):
    return name.lower().capitalize();

# namelist  =['adam', 'LISA', 'barT']
# normalize(namelist)

r5 = map(normalize,['adam', 'LISA', 'barT'])
print(r5)