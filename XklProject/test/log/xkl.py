# -*- coding:utf-8 -*-
import logging
import sys
import log
from wechat_sender import *
reload(sys)
sys.setdefaultencoding('utf8')


if __name__ == "__main__":
    logger = logging.getLogger("xkl")
    for i in range(0,10):
        logger.info("我输出了")





