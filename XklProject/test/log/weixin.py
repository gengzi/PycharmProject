#!/usr/bin/env Python
# coding=gbk
from wxpy import *
import sys
reload(sys)
sys.setdefaultencoding('gbk')


from wxpy import *
from wechat_sender import *
# ����������֤
bot = Bot(cache_path="/home/ubuntu/python_workspace/xiakeliao/xkl/",console_qr=-2)
# ��ʱ���������״̬
listen(bot=bot,status_report=True)




