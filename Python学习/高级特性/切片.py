#coding=utf-8


L = list(range(100))

# print(L)

# 使用切片
# [开始索引:终止索引:步长]
print(L[0:10])   #下标为0，从0开始到9结束，不包含10
print(L[:10])    #如果下标为0 ，可以省略
print(L[:10:2])  #第三个参数是步长， [0, 2, 4, 6, 8]

print(L[-1:])   #取出最后一个元素
print(L[-10:])  #取出后10 个元素

print(L[::]) #取出所有
print(L[::5]) #以步长为5，取出

print(L[::-1]) #逆序取出

# 字符串和元组都可以使用切片，但是不会修改自身

name = 'abcdefg'
print(name[0:5]) # 取出前四个
# print(name[1:2])
# print("输出：%s",name[:1])
print(name[2:-1])
print(name[0:0])


nametuple = (1,12,'222')
print(nametuple[:2])  #取出前两个

# 实现一个 trim() 去除前后的空格
def trim(x):
    if len(x) == 1:
        if  x[0] ==  ' ':
            return ''
        else:
            return x
    else:
        i = 0;
        j = 0;
        # 使用切片，一个字符一个字符判断
        for item in x:
            if item == ' ':
                i +=1;
            else:
                break
        # print(x[i:])   取出 索引是 i 的字符串
        # print(x[::-1]) 逆序取出字符串
        for item in x[::-1]:
            if item == ' ':
                j +=1;
            else:
                break
        return  x[i:-j]

while True:
    name_trim = str(raw_input("请输入你的名字："))
    # 获取字符串的长度
    strlen = len(name_trim)
    if strlen == 0:
        print("请输入一个正确的字符串!!")
        continue
    print(trim(name_trim))
    break



# 递归

def trimdemo2(s):
    if len(s) == 0:
        return ''
    else:
        if s[0] == ' ':
            s = s[1:]
            return trim(s)
        elif s[-1] == ' ':
            s = s[:-1]
            return trim(s)
        else:
            return

print(trimdemo2('   ssssss   fff   '))
# 你这是Python2，人家的示例代码是Python3，你要用raw_input代替input。Python2的input这种蛇精病的内置函数不要用比较好，它相当于eval(raw_input())，把输入的数据直接当作代码来执行。Python3把这个函数删了，用raw_input替换掉了input。
#
# 作者：灵剑
# 链接：https://www.zhihu.com/question/31388311/answer/112859858
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。