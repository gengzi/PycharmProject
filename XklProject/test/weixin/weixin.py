#!/usr/bin/env Python
# coding=gbk



from wxpy import *
import sys
reload(sys)
sys.setdefaultencoding('gbk')

# # ΢�Ż�����
# path ="H:\\python\\xiakeliao\\weixin\\denglu.png"
# bot = Bot(cache_path=True,qr_path=path)
#
# # �� Web ΢���а��Լ���Ϊ����
# bot.self.add()
# bot.self.accept()
#
# # ������Ϣ���Լ�
# bot.self.send('���յ���')
#
#
#
# embed()


from wxpy import *

# bot = Bot()
# ��ȡ����
# my_friend = bot.friends().search('����'.decode("gbk"))[0]
#
# # ������Ϣ
# messages = bot.messages.search(keywords='�յ�'.decode("gbk"), sender=bot.self)
#
# for message in messages:
#     print(message)
#
#
#
# # ��Ϣ���ռ�����
# @bot.register()
# def print_others(msg):
#     # �������������Ϣ
#     print(msg)
#     # �ظ���Ϣ
#     msg.reply("hello world")


# ���һ��ר�� Logger
# �������� `receiver` ʱ���Ὣ��־���͵����ɨ���½��΢�ŵ�"�ļ���������"
logger = get_wechat_logger()

# ���;���
logger.warning('����һ�� WARNING �ȼ�����־�����յ�����')

# ���ղ�����쳣
try:
    1 / 0
except:
    logger.exception('���������յ���ʲô��')


embed()


