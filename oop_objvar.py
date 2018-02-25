# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言”

class RoBot:
    '''表示一个带有名字的机器人。'''

    # 定义一个类变量，用来计算现在机器人的数据
    population = 0

    # 定义一个方法
    def __int__(self, name):
        self.poname = name
        print('(初始化 {} )'.format(self.poname))

        # 当机器人被创建，数量+1
        RoBot.population += 1

    # 死亡
    def die(self):
        """我挂了。"""
        print("{} is being destroyed!".format(self.name))
        RoBot.population -= 1
        if RoBot.population == 0:
            print("{} 是最后一个.".format(self.name))
        else:
            print("还有 {:d} 个机器人正在工作".format(
                RoBot.population))


    def say_hi(self):
        """来自机器人的诚挚问候 没问题，你做得到。"""
        print("Greetings, my masters call me {}.".format(self.name))


# classmethod  装饰器等价于调用 ,将他标识为 类方法



# self.__class__  属性来引用它的类

# 所有类成员（包括数据成员）都是公开的