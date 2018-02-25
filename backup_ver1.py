#-*- coding:utf-8 -*-
#Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言”

#导入模块
import os
import time

#需要备份的列表
source = 'E:\\apache-tomcat-7.0.73-windows-x64'
#ff
#需要存放的文件夹
target_file='E:\\back'

#生成文件名称
target = target_file + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'

#如果目标目录不存在就去创建
if not os.path.exists(target_file):
    os.mkdir(target_file)

# 5. 我们使用 zip 命令将文件打包成 zip 格式
zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))
# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
