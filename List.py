#-*- coding:utf-8 -*-
#Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言”


# 列表

#创建一个列表,可以存放任意的类型
shoplist = ['苹果','橘子',23,True,23.6]

print(shoplist)
#长度
print("list的长度:"+str(len(shoplist)))

#遍历list
for item in shoplist:
    print("参数："+str(item))

#新增一个数据
shoplist.append('梨')
#插入一个数据
shoplist.insert(1,'橘子。')
#索引从0 开始
print("索引为0："+shoplist[0])

#索引还可以取负数
print("索引为-1：{}".format(shoplist[-1]))

#移除第一个元素，删除指定位置的元素
del shoplist[0]
#删除list末尾的元素
shoplist.pop()
#索引还可以取负数
print("删除末尾元素后，索引为-1：{}".format(shoplist[-1]))

#替换指定位置上元素的值
shoplist[1]='新橘子'
#索引还可以取负数
print("索引为1：{}".format(shoplist[1]))


#遍历list

for item in shoplist:
    print("变化后的参数："+str(item))

# 对列表进行排序
shoplist.sort();

#遍历list
for item in shoplist:
    print("排序后的参数："+str(item))

# list 的中元素还可以是一个 list

shoplist[0] = ['par1',222,'33']
print(shoplist)
# 取数据
print("0,0:"+shoplist[0][0])

    

