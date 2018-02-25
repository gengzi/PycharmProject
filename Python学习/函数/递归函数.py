#coding=utf-8
#Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言

# 递归函数
from itertools import product


def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)


print(fact(5))  # 5 的阶乘

print(fact(100))

#  尾递归优化
def fact(n):
    fact_item(n,1)

def fact_item(num,product):
    if num==1:
        return product
    return fact_item(num-1,num*product)


fact()