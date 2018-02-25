# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言”

def findMinAndMax(list):
    if not len(list):
        return (None,None)
    else:
        min  = max = list[0]
        for v in list:
            if min > v :
                min = v
            if max < v :
                max = v
        return  (min,max)

liststr = [1,23,44,44]
print(findMinAndMax(liststr))

