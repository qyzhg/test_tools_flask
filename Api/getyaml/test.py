#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   test.py
 
@Time    :   2020/6/22 2:58 下午
'''
import ast

from Api.settings import JSON_FILE

with open(JSON_FILE, 'r', encoding='utf-8') as f:
    # print(str(f.read()))
    # 将字符串转换为字典
    try:
        dict_f = ast.literal_eval(str(f.read()))
        dict_var = {
            # 'remark': remark,
            # 'name': name,
            # 'url': url,
            # 'meth': meth,
            'params':
                dict_f
        }

    except ValueError:
        print(1)
        with open(JSON_FILE, 'r', encoding='utf-8') as f1:
            content = f1.read()
        # print(content)
        t = content.replace(': false',': False').replace(': true',': True').replace(':false',':False').replace(':true',':True')
        with open(JSON_FILE, "w") as f2:
            f2.write(t)