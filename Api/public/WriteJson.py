#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   WriteJson.py
 
@Time    :   2020/6/9 4:24 下午
'''
from Api.settings import JSON_FILE

def write_json(json_data):
    with open(JSON_FILE,'w',encoding='utf-8') as json_file:
        json_file.write(json_data)