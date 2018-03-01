# -*- coding:utf-8 -*-


from DateUtils import  *
import sys
reload(sys)
sys.setdefaultencoding('utf8')


"""
    文件操作常用方法
    author：gengzi
    version：0.0.1
    sj：2018年3月1日16:44:03
"""



def foreachPath2file(dirpath):
    """
    根据目录的路径循环遍历，其中符合要求的文件
    :param dirpath: 目录的路径 str ,请在目录的末尾加上 \ 或者 \\ win  F:\\doc\\cc  linux : \home\usr\
    :return: list 目录集合
    """
    filepaths = []
    for filename in os.listdir(dirpath):
        filepaths.append(dirpath+""+filename)
    return filepaths
#调用测试
# filepaths = foreachPath2file("H:\\python\\ubuntu\\2018-02-27\\")
#
# for path in filepaths:
#     print path










