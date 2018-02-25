#coding=utf-8
#Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言
# return None可以简写为return
import math

# 空函数
# 实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def top():
    pass

# 在别的语句里面，也可以放上空
# age = int(input("请输入"))
# if age >  0 :
#      pass


top()

#  在定义函数的时候，可能需要对参数做限制
#   对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
def fun01(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type,mast is int or float')
    print(x)

# fun01('22')

# 定义的函数返回多个值
# 比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：
def fun02(x,y,step,angle=30):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny


xVal,yVal= fun02(10,11,2)
print(xVal)
print(yVal)
#  返回的是一个元组
# 在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
print(fun02(10,11,2))




def quadratic(a, b, c):
    if b*b-4*a*c >= 0:
        x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
        x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
        print(x1,x2)
    else:
        print("无解")

quadratic(1,-44,144)