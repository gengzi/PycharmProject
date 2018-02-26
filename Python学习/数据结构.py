# -*- coding: UTF-8 -*

shopList =['苹果','芒果','香蕉','西瓜']

print('list的长度：'+str(len(shopList)))

for i in shopList:
    print("value:"+str(i))


shopList.append('哈密瓜')
print(str(shopList))
# sort 方法对列表进行排序。
shopList.sort()
for i in shopList:
    print("value:"+str(i))

print(shopList[0])
