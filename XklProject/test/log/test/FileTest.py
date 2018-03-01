

import sys
reload(sys)
sys.setdefaultencoding('utf8')

try:
    with open("111") as f:
         content = f.read()
except Exception,e:
    print e
    print("111")

