#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   data_to_json.py
 
@Time    :   2019/11/5 2:07 下午
'''
from Api.settings import *


def DataToJson():
    print('非json格式，正在尝试转换为json格式...')
    with open(JSON_FILE, 'r', encoding='utf-8') as datas:
        datas = datas.readlines()

    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        f.writelines('{')
        for data in datas:
            try:
                f.writelines('"%s": "%s",' % (data.split('\t')[0], data.split('\t')[1].replace('\n', '')))
            except:
                f.writelines('"%s": "%s",' % (data.split('\t')[0].replace('\n', ''), ''))
        f.writelines('}')
    return '非json格式，正在尝试转换为json格式...'


if __name__ == '__main__':
    DataToJson()
