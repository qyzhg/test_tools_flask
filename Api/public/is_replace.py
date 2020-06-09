#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   is_replace.py
 
@Time    :   2020/6/2 9:06 上午
'''
from Api.public.menu import menu


def is_replace(case_path, name, url, meth, remark):
    print('目录中已存在同名测试用例文件：{case_path},请选择是否覆盖??'.format(case_path=case_path))
    while True:
        is_replace = input('Y:覆盖(默认) \nN:取消操作\n').upper()
        if is_replace == 'Y' or is_replace == 'YES' or is_replace == '':
            menu(name=name, url=url, meth=meth, case_path=case_path, remark=remark)
            break
        elif is_replace == 'N' or is_replace == 'NO':
            print('已取消操作！')
            break
            # sys.exit(0)
        else:
            print('输入有误，请重新选择')
