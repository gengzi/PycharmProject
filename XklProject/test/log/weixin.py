#!/usr/bin/env Python
# coding=gbk
from wxpy import *
import sys
reload(sys)
sys.setdefaultencoding('gbk')


from wxpy import *
from wechat_sender import *

bot = Bot(cache_path=True)
listen(bot)


