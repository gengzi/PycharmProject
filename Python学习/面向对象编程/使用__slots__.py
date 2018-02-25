#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from types import MethodType

class Student(object):
    pass
# 可以给实例 绑定一个字段
s= Student()
s.name = '张三'
print(s.name)

# 可以给实例 绑定一个方法 ,只能对一个实例起作用
def set_age(self,age):
    self.age = age

s = Student()
s.set_age = MethodType(set_age,s)  #给实例 绑定一个方法
s.set_age(22)
print(s.age)

# s2 = Student()
# s2.set_age(22)
# print(s2.age)
# 报错  AttributeError: 'Student' object has no attribute 'set_age'


# 如果给class 绑定方法，所有的实例都可以使用
def set_age(self,age):
    self.age = age
def set_name(self,name):
    self.name = name

Student.set_age = set_age  #给所有的实例绑定方法
Student.set_name = set_name #给所有的实例绑定方法

s3 = Student()
s3.set_age(23)
print(s3.age)

s4 = Student()
s4.set_name('李四')
print(s4.name)

