#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class student(object):
    pass

# 表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。


# 在属性的前面加上两个下划线，就变成了 私有的变量


class Person(object):
    def  __init__(self,name,age):
        self.__name = name
        self.__age = age

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


p =  Person('张三',22);
print(p.get_name())
print(p.get_age())

p.set_age(44)
p.set_name('李四')
print(p.get_name())
print(p.get_age())



# 如果试图获取不存在的属性，会抛出AttributeError的错误：
