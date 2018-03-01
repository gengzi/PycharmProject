# -*- coding:utf-8 -*-
import logging
import sys
import log
from wechat_sender import *
reload(sys)
sys.setdefaultencoding('utf8')



logger = logging.getLogger("xkl")



if __name__ == "__main__":
    # 每次调用get_logger()方法时都会给它加一个新的handler
    # logger = logging.getLogger("xkl")
    for i in range(0,5):
        logger.info("我输出了"+str(i))






