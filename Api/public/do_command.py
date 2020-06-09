#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   do_command.py
 
@Time    :   2020/6/9 4:54 下午
'''
import os
from Api.settings import BASE_DIR


def cmd(name,url,meth,remark):
    a = os.system(f'cd {BASE_DIR} && python main.py --n {name} --u {url} --m {meth} --r {remark}')
    return a