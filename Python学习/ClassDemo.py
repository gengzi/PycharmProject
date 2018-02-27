# -*- coding: UTF-8 -*-
class Person:
    # pass  #创建的是一个空代码块，使用  pass  语句予以标明
    def say_hi(self):
        print("hello world"+self.name)

    def __init__(self,name):
        self.name = name

p =Person('111')
p.say_hi()