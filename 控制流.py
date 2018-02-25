#-*- coding:utf-8 -*-
#Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言”

#if 语句

# number = 22
# # 可以使用 int 将字符串 转化为 数字
# flag = int(input("请输入数字："))
#
# if flag > number :
#     print("比22 大")
# elif flag < number :
#     print("比22 小")
# else:
#     print("与22 相等")
#
# #elif  和  else  同样都必须有一个冒号在其逻辑行的末尾
#
# flag = True
# if flag:
#     print("为true")
#
# #Python 中不存在  switch  语句



# while语句  --------------------------------------

# number = 22
# flag = True
# # 可以使用 int 将字符串 转化为 数字
# while flag:
#     num = int(input("请输入数字："))
#     if num > number :
#         print("比22 大")
#        # flag = False
#         break  #一旦使用 break 结束循环，就不会再走  while 的else 了
#     elif flag < number :
#         print("比22 小")
#         continue
#     else:
#         print("与22 相等")
# else:
#     print("循环结束")




# for语句  --------------------------------------
# for in
for i in range(1, 33):  # range  函数生成这一数字序列  如 ：range(1,5)  将输出序列  [1, 2, 3, 4]
    ## range(1,5,2)  将会输出  [1, 3]
    print(i)
else:
    print('遍历完毕')

    # for in
for i in range(1, 33,4):  # range  函数生成这一数字序列  如 ：range(1,5)  将输出序列  [1, 2, 3, 4]
        ## range(1,5,2)  将会输出  [1, 3]
     print(i)
else:
     print('遍历完毕')

print(list(range(1,5)))  #[1, 2, 3, 4]

#如果你的 中断 了一个  for  或  while  循环，任何相应循环中的else  块都将不会被执行。