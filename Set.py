#-*- coding:utf-8 -*-
#Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言”


# 如果是对象的引用  你必须使用切片操作来制作副本
# set 集合，只存储key ，并不存放value 。  不会存放重复元素

studentid = set([144803085,144803092,144803127])
print(studentid)
# 不会存放重复元素
studentid = set([144803085,144803085,144803092,144803127])
print(studentid)

# 添加一个元素
studentid.add(144803011)
print(studentid)

#删除一个元素
studentid.remove(144803011)
print(studentid)

# 循环set 集合
for item in studentid:
    print(item)

teatherId = set((11441,11442,11443))
print(teatherId)
listkey = [11,22,33]
teatherId = set(listkey)
print(teatherId)

