#coding=utf-8
#Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言”

# 元组  你不能编辑或更改元组
# 元组通常用于保证某一语句或某一用户定义的函数可以安全地采用一组数值，意即元组内的
# 数值不会改变。

# 创建一个元组
zoo = ('老虎','狮子','海豚')

# 元组的长度 len  函数在此处用来获取元组的长度。
print("zoo的长度:"+str(len(zoo)))

#更新一个元组

zoos = ('老鼠','鸭子',zoo)

# 新的元组长度
print("zoos的长度:"+str(len(zoos)))
print(zoos)

#取zoos的第二个元组数据
print(zoos[2])
print(zoos[2][2])

# 整个元组的长度
print("整个元组的长度："+str(len(zoos)-1+len(zoos[2])))


#特殊情况
#一个空的元组
empty1 = ()

#只包含一个项目的元组  , 必须在后面加上一个 逗号， 用来区分是对象 还是元组

singleton = ('11',)




#创建一个元组 包含list
shops = ('apple','banan',['fanqie',22])
print(shops)

#取值
print(shops[2][0])
shops[2][0] = 'fanqies'
shops[2][1] = 55
print(shops)

print(shops)


#测试一下，修改元组中的list，看list 会发生改变么
# hui



