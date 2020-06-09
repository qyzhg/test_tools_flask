#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   update.py
 
@Time    :   2020/6/8 10:24 上午
'''

import os
from Api import settings


def Update():
    # if update.upper() == 'TOOLS':
    print('更新工具有丢失数据的风险！请将case妥善备份！！请将case备份后继续！！！\nY:继续（默认）\nN:取消')
    while True:
        try:
            if (a := input('\n').upper()) == 'Y' or a == '':
                toolsdir = (os.path.dirname(settings.BASE_DIR))
                os.system(f'cd {toolsdir} && git fetch --all && git reset --hard origin/master && git pull')
                # print('挡板触发')
                return
            elif a == 'N':
                print('操作已取消!!')
                return
            else:
                print('输入错误，请重新输入')
        except SyntaxError:
            print('请更新python版本到3.8以上在重试')
            return
