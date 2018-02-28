#!/usr/bin/env Python
# coding=gbk



from wxpy import *
import sys
reload(sys)
sys.setdefaultencoding('gbk')

# # 微信机器人
# path ="H:\\python\\xiakeliao\\weixin\\denglu.png"
# bot = Bot(cache_path=True,qr_path=path)
#
# # 在 Web 微信中把自己加为好友
# bot.self.add()
# bot.self.accept()
#
# # 发送消息给自己
# bot.self.send('能收到吗？')
#
#
#
# embed()


from wxpy import *

# bot = Bot()
# 获取好友
# my_friend = bot.friends().search('李洋'.decode("gbk"))[0]
#
# # 搜索信息
# messages = bot.messages.search(keywords='刚到'.decode("gbk"), sender=bot.self)
#
# for message in messages:
#     print(message)
#
#
#
# # 消息接收监听器
# @bot.register()
# def print_others(msg):
#     # 输出监听到的消息
#     print(msg)
#     # 回复消息
#     msg.reply("hello world")


# 获得一个专用 Logger
# 当不设置 `receiver` 时，会将日志发送到随后扫码登陆的微信的"文件传输助手"
logger = get_wechat_logger()

# 发送警告
logger.warning('这是一条 WARNING 等级的日志，你收到了吗？')

# 接收捕获的异常
try:
    1 / 0
except:
    logger.exception('现在你又收到了什么？')


embed()


