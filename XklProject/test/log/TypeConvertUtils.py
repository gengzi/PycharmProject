#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def classToDict(obj):
    """
    对象转 字典
    :param obj: 对象
    :return: 字典
    """

    is_list = obj.__class__ == [].__class__
    is_set = obj.__class__ == set().__class__

    if is_list or is_set:
        obj_arr = []
        for o in obj:
            dict = {}
            dict.update(o.__dict__)
            obj_arr.append(dict)
        return obj_arr
    else:
        dict = {}
        dict.update(obj.__dict__)
        return dict