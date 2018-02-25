#coding=utf-8
#Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言

# 函数参数 ： 位置参数

def power(x):
    print(x*x)

# power(5)

def power(x,n):
    s = 1
    while n>0:
        s = s*x
        n = n-1
    return s

# print(power(5,5))

# power(5)   #报错：TypeError: power() takes exactly 2 arguments (1 given)


# 默认参数 ，来解决上面出现的问题

def power(x,n=2):
    s = 1
    while n>0:
        s = s*x
        n = n-1
    return s

print(power(5))
print(power(5,5))

# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

# 二是如何设置默认参数。


# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
#使用默认参数有什么好处？最大的好处是能降低调用函数的难度
def enroll(name, gender,age=6,city='bg'):
    print('name:', name)
    print('gender:', gender)
    print('age:',age)
    print('city:',city)


# enroll('jack','F')
enroll('jack','F',age=55)
enroll('jack','F',city='bg1')


#  使用默认参数有一个坑


# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#
#  定义默认参数要牢记一点：默认参数必须指向不变对象！


#  可变参数
# 在传入参数的时候，可能我们不知道到底有几个参数

def calc(number):
    sum = 0
    for i in number:
        sum = sum + i*i
    return sum
print(calc([1,12,33,44]))

# 变成可变的参数：
def calc(*number):
    sum = 0
    for i in number:
        sum = sum + i*i
    return sum

print(calc(1,12,33,44))

# 如果是可变对象
num = [1,12,33,44]
print(calc(*num))













