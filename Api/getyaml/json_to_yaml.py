#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   测试yaml.py
 
@Time    :   2020/5/26 10:39 上午
'''
try:
    import ruamel.yaml
except ImportError:
    print('发现缺少的依赖库，工具正在尝试安装，如安装失败，请使用pip install ruamel.yaml命令自行安装')
    import os

    os.system('pip install ruamel.yaml')
    import ruamel.yaml
import ast
import os
import sys
import time

sys.path.append(os.path.abspath('../..'))
from Api.settings import *
from Api.public.WriteTestCase import WriteTestCase
from Api.getyaml.data_to_json import DataToJson

t = time.ctime()


def json_to_yaml(name, url, meth, case_path, remark):
    '''
    将json文件中的文件转换生成yaml格式的测试用例
    :param name: 接口名
    :param url:
    :param meth:
    :param case_path:
    :return:
    '''
    meth = meth.upper()
    if 'JSON' not in meth and 'DATA' not in meth and 'GET' not in meth:
        print('meth参数输入有误，请使用--help参数查看帮助')
        return {'2':'meth参数输入有误，请使用--help参数查看帮助'}
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        try:
            # print(str(f.read()))
            #将字符串转换为字典
            dict_f = ast.literal_eval(str(f.read()))
            dict_var = {
                'remark': remark,
                'name': name,
                'url': url,
                'meth': meth,
                'params':
                    dict_f
            }
            # print(dict_var)
        except SyntaxError:
            #转换form到json
            DataToJson()
            with open(JSON_FILE, 'r', encoding='utf-8') as f:
                dict_f = ast.literal_eval(str(f.read()))
                dict_var = {
                    'remark':remark,
                    'name': name,
                    'url': url,
                    'meth': meth,
                    'params':
                        dict_f
                }
        except ValueError:
            #将文件中引起异常的小写fale和true替换成python兼容的格式
            print(1)
            with open(JSON_FILE, 'r', encoding='utf-8') as f1:
                content = f1.read()
            # print(content)
            t = content.replace(': false', ': False').replace(': true', ': True').replace(':false', ':False').replace(
                ':true', ':True')
            with open(JSON_FILE, "w") as f2:
                f2.write(t)
            with open(JSON_FILE, 'r', encoding='utf-8') as f:
                dict_f = ast.literal_eval(str(f.read()))
                dict_var = {
                    'remark':remark,
                    'name': name,
                    'url': url,
                    'meth': meth,
                    'params':
                        dict_f
                }


    try:
        with open(case_path, 'w+', encoding='utf-8') as case_file:
            print(ruamel.yaml.dump(dict_var, Dumper=ruamel.yaml.RoundTripDumper, allow_unicode=True), file=case_file)
            print('已生成接口配置文件：' + case_path)
            return {'0':'成功生成接口配置文件!'}
    except FileNotFoundError:
        print('项目目录不存在，请检查项目目录和settings文件中的PROJECT_NAME配置!')
        return {'2':'项目目录不存在，请检查项目目录和settings文件中的PROJECT_NAME配置!'}


def make_locustfile(name, remark=''):
    try:
        WriteTestCase(filepath=LOCUSTFILE_FILE,

                      linenum=-22,

                      content=f"\n#{t}:该代码由工具自动生成，请检查后使用！\n    "
                              "@task(1)\n    "
                              f"def __{name}(self):\n"
                              f"        '''\n"
                              f"        {remark}\n"
                              f"        '''\n"
                              f"        self.Api.api('{name}')\n\n"
                      )
    except FileNotFoundError:
        print('目录不存在')
        return {'2':'目录不存在！'}
    print(F'该方法已生成到性能测试文件下:{LOCUSTFILE_FILE}')
    return {'0':'成功生成性能测试文件!'}


def make_apifile(name, remark=''):
    WriteTestCase(filepath=TEST_API_FILE,
                  linenum=-1,
                  content=f"\n#{t}该代码由工具自动生成，请检查后使用！"
                          f"\n    def test_{name}(self):\n"
                          f"        '''\n"
                          f"        {remark}\n"
                          f"        '''\n"
                          f"        r = self.api('{name}')\n"
                  )
    print(F'该方法已生成到接口测试文件下:{TEST_API_FILE}')
    return {'0':'成功生成接口测试文件!'}
