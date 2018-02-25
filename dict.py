#-*- coding:utf-8 -*-
#Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言”

#创建一个字典  键值必须是唯一的 就是 map
# 另外要注意的是你只能使用不可变的对象（如字符串）作为字典的键值，但是你可以使用可
# 变或不可变的对象作为字典中的值。

# 特点，具有极快的查询速度，原因在存储 map 的时候， 首先，根据key 计算出 value 需要存放的位置， 可以类比java的 hashmap ，在存放值
# 的时候，计算key 的hashcode ，来决定存放 hashmap 的位置


ad = {
    '耿帅佳':'沙河于辛庄',
    '杜悦':'立水桥',
    'jack':1111,
    'rose':3333
}


#打印一下耿帅佳的地址
print("耿帅佳的地址："+str(ad['耿帅佳']))

# 删除一个键值对
del ad['rose']
ad.pop('杜悦')

print('现在的字典长度：'+str(len(ad)))

# 判断在该 map 中是否存在 key
print('jack' in ad)

# 使用 get 方法返回key 的值
print(ad.__getitem__('jack'))
# 如果 不存在，会返回一个 none ， 也可以自己设定为 需要显示的值 -1
print(ad.get('jack1'))
print(ad.get('jack1',-1))

# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
#
# 和list比较，dict有以下几个特点：
#
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
#
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。



#遍历一下字典
for name,address in ad.iteritems(): #在3 中方法改变了
    print("我的名字是 {0} ，我的住址在 {1}".format(name,address))

# 新添加一个
ad['rose'] = '沙河地铁站'


#  item  方法来访问字典中的每一对键值—值配对信息，这一操作
# 将返回一份包含元组的列表，每一元组中则包含了每一对相应的信息——键值以及其相应的
# 值。

#遍历一下字典
for name,address in ad.iteritems(): #在3 中方法改变了
    print("名字是 {0} ，住址在 {1}".format(name,address))