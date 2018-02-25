#-*- coding:utf-8 -*-
#Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言”

age=20
name="耿帅佳"

print(''' My name is {0} '''.format(name))
print(''' {0} age is {1} '''.format(name,age))

#直接组拼后输出
zupin_str = name + 'is' + str(age) + "哈哈哈";
print(zupin_str)
print( name + 'is' + str(age) + "哈哈哈")

#格式化 浮点类型 结果 0.667
print('{0:.3f}'.format(10.0/15.0))
print('{0:.5f}'.format(10.0/15.0))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))
print('{0:&^11}'.format('hello'))

#防止输出出现 \n 换行
print('hello world')
#使用反斜杠来实现转义
print('what\'s')
#使用 \n \t
print('what\'s  \n  zhuan  ')
print('what\'s  \t  zhuan  ')
#使用 \ 来实现同一行输出
print("This is the first sentence. \
This is the second sentence.")
#输出原始的字符串,在字符串前面加上一个 r 或者 大写的R  在处理正则表达式时应全程使用原始字符串
print(r'what\'s \n \t zhuan  ')

