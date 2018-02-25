#-*- coding:utf-8 -*-
#Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言”

#函数（Functions）是指可重复使用的程序片段

#定义一个 函数
def  sayHelloWorld():
# 该块属于这一函数
    print('hello world')
# 函数结束

# sayHelloWorld();
# sayHelloWorld();

#带有参数的 函数方法
def panduan(parm1,parm2):
    if parm1 > parm2:
        print(str(parm1)+"大于"+str(parm1))
    elif parm1 < parm2 :
        print(str(parm1)+"小于"+str(parm2))
    else:
        print(str(parm1)+"等于"+str(parm2))
#函数结束

#  int 类型不会自动强转成 string 类型
panduan(22,33);


# 局部变量

x = 50;

def print_str(x):
    print("我是传递的参数"+str(x))
    x = 333;
    print("我是修改后的局部变量"+str(x))

#所有变量的作用域是它们被定义的块，从定义它们的名字的定义点开始。
print_str(x)

# 在函数内修改全局变量

x = 50;

def print_str():
    global x
    print("我是传递的参数"+str(x))
    x = 333;
    print("我是修改后的局部变量"+str(x))

#所有变量的作用域是它们被定义的块，从定义它们的名字的定义点开始。
print_str()
print(x)

# 默认的参数值
# 注意：只有那些位于参数列表末尾的参数才能被赋予默认参数值，意即在函数的参数列表中拥
# 有默认参数值的参数不能位于没有默认参数值的参数之前。
# 例如： def func(a, b=5)  是有效的，但  def func(a=5, b)  是无效的。

x = 50;

def print_str(y = 3):
    global x
    print("我是传递的参数"+str(x))
    x = 333;
    print("我是修改后的局部变量"+str(y))

#所有变量的作用域是它们被定义的块，从定义它们的名字的定义点开始。
print_str(2)
print(x)


# * 号 用来写 可变参数
#


# None  在 Python 中一
# 个特殊的类型，代表着虚无

# 举个例子， 它用于指示一个变量没有值，如果有值则它的值便
# 是  None（虚无）  。


# 文档字符串

def print_str1(x,y):
    ''' 输出文本函数。

    两个参数都是字符串'''
    print("打印："+x+":"+y);


print_str1("x","y")
print (print_str1.__doc__)

# help(print_str1)



