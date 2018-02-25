#coding=utf-8

# x=list(range(1,100))   生成一个从 1 到 99 的列表
# print(x)

liststr = [x*x for x in range(1,11)] # 1到10 的平方
print(liststr)

liststr = [x*x for x in range(1,11) if x%2==0 ] # 1到10 的平方
print(liststr)

liststr1 = [m+n for m in ['AB','BC','CD'] for n in ['EF','HG']]
print(liststr1)

# 列出当前目录下的所有文件和目录名
import os
listdirstr = [d for d in os.listdir('E:\zheng')]  #不能识别中文
print(listdirstr)

# 将list 中的字符串都变成小写
L1 = ['Hello', 'World', 18, 'Apple', None]
L1str = [ s.lower()  for s in L1 if  isinstance(s,str)]
print(L1str)



# 杨辉三角定义如下：
# def triangles(x):
#     for item in x:
#         px = []
#         for j in item:
#             px.append(j)
#             print([i])
#
#     pass
#
#
#
# triangles(10)
# print()


def YangHui (num = 10):
    LL = [[1]]
    for i in range(1,num):
        # [1, 1]
        LL.append([(0 if j== 0 else LL[i-1][j-1])+ (0 if j ==len(LL[i-1]) else LL[i-1][j]) for j in range(i+1)])
        print(LL)
    return LL

YangHui()


LL = [[1]]
i = 1
# iis1 = [(0 if j== 0 else LL[i-1][j-1])+ (0 if j ==len(LL[i-1]) else LL[i-1][j]) for j in range(i+1)]
# iis1 = [(0 if j== 0 else LL[0][1])+ (0 if j ==len(LL[0]) else LL[0][1]) for j in range(1)]
# print(iis1)

