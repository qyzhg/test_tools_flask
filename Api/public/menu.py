#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao

@Contact :   qyzhg@163.com

@File    :   menu.py

@Time    :   2020/5/30 7:10 下午
'''

import sys, os

sys.path.append(os.path.abspath('../../'))
from Api.getyaml.json_to_yaml import json_to_yaml, make_locustfile, make_apifile


def menu(name, url, meth, case_path, remark):
    print('是否需要将代码追加到文件中？\n'
          '【1】：将文件追加到性能测试脚本文件和接口测试脚本文件中(默认)\n'
          '【2】：将文件只追加到性能测试脚本文件中\n'
          '【3】：将文件只追加到接口测试脚本文件中\n'
          '【4】：仅生成yaml文件，不向测试脚本文件中追加\n'
          '【exit】：退出\n'
          )

    while True:
        is_mk_code = input('请输入功能序号\n')
        if is_mk_code == '1' or is_mk_code == '':
            json_to_yaml(remark=remark,
                         name=name,
                         url=url,
                         meth=meth,
                         case_path=case_path)
            make_locustfile(name=name, remark=remark)
            make_apifile(name=name, remark=remark)
            break

        elif is_mk_code == '2':
            json_to_yaml(remark=remark,
                         name=name,
                         url=url,
                         meth=meth,
                         case_path=case_path)
            make_locustfile(name=name, remark=remark)
            break

        elif is_mk_code == '3':
            json_to_yaml(remark=remark,
                         name=name,
                         url=url,
                         meth=meth,
                         case_path=case_path)
            make_apifile(name=name, remark=remark)
            break

        elif is_mk_code == '4':
            json_to_yaml(remark=remark,
                         name=name,
                         url=url,
                         meth=meth,
                         case_path=case_path)
            break

        elif is_mk_code.upper() == 'EXIT':
            print('已退出！')
            sys.exit(0)

        else:
            print('输入有误，请重新选择')
