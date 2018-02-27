# -*- coding: UTF-8 -*-

import os
import time

# 需要压缩的文件
source = 'F:\\test'

#备份的目录
target_dir = 'F:\\test2'
# 要记得将这里的目录地址修改至你将使用的路径
# 3. 备份文件将打包压缩成 zip 文件。
# 4. zip 压缩文件的文件名由当前日期与时间构成。
target = target_dir + os.sep + \
    time.strftime('%Y%m%d%H%M%S') + '.zip'
# 如果目标目录还不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir) # 创建目录
# 5. 我们使用 zip 命令将文件打包成 zip 格式
zip_command = 'winrar a  {0} {1}'.format(target,source)
# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
#这一函数可以使命令像是从系统中运行的。
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

