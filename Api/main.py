#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao

@Contact :   qyzhg@163.com

@File    :   main.py

@Time    :   2020/5/30 5:27 下午
'''

import argparse
import os
import sys

# 版本检查提醒
Py_version = sys.version_info
if Py_version.major == 3 and Py_version.minor < 8:
    print('检测到您的python环境低于3.8，请及时将python版本升级到3.8以上，否则一些功能无法正常使用！')

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Api.settings import *
from Api.public.menu import menu
from Api.public.is_replace import is_replace

parser = argparse.ArgumentParser(description='先将需要转换的json放入json文件中 命令为python --n 接口名 --u 接口地址 --m 请求方式')
parser.add_argument('--n', '--name', type=str, help='接口名，例如：login，输入%%auto可以根据接口地址自动生成接口名')
parser.add_argument('--u', '--url', type=str, help='接口地址，例如：a/login，配置好settings中的HOST后，可以直接输入完整地址')
parser.add_argument('--m', '--method', type=str, help='请求方式，只能输入三种请求方式：GET，POST/data，POST/json')
parser.add_argument('--remark', '--r', type=str, help='备注，说明')
parser.add_argument('-start', type=str, help='生成项目目录，使用方式为 -start 项目名')
parser.add_argument('-cs', type=str, help='create_script 根据yaml测试用例生成测试脚本，使用方式为 -cs 项目名')
parser.add_argument('-runtest', type=str, help='执行接口测试脚本并生成报告和发送邮件，使用方式为 -runtest 项目名')
parser.add_argument('-runlocust', type=str, help='运行性能测试服务，使用方式为 -runlocust 项目名')
parser.add_argument('-update', action='store_true', default=False, help='更新工具主程序，使用方式为 python main.py -update')

args = parser.parse_args()

# 创建项目目录
start = args.start
if start:
    from Api.public.start import start_project

    start_project(start)
    sys.exit(0)

# 通过测试用例生成脚本
cs = args.cs
if cs:
    from Api.public.create_script import create_script

    create_script(cs)
    sys.exit(0)

#执行测试脚本
runtest = args.runtest
if runtest:
    from Api.public.RunTest import runAPITEST
    runAPITEST(runtest)
    sys.exit(0)

#运行性能测试服务
runlocust = args.runlocust
if runlocust:
    from Api.public.RunTest import runLOCUST
    runLOCUST(runlocust)
    sys.exit(0)

# 更新工具
update = args.update
if update:
    from Api.public.update import Update

    Update()
    sys.exit(0)

url = args.u
if url == None:
    print('请带参数运行此工具，需要帮助请使用--help命令')
    sys.exit(0)
if HOST in url:
    url = url.split(HOST)[1]

meth = args.m
if meth == None:
    print('请带参数运行此工具，需要帮助请使用--help命令')
    sys.exit(0)

name = args.n
if name == None:
    print('请带参数运行此工具，需要帮助请使用--help命令')
    sys.exit(0)
if name.upper() == '%AUTO':
    name = (url + '_' + meth.upper()).replace('/', '_')
# yaml输出路径
case_path = os.path.join(CASE_DIR, name) + '.yaml'

if None in [name, url, meth]:
    print('缺少必要的参数，请使用--help参数查看帮助')
    sys.exit(0)

remark = args.remark

# 有存在的测试用例的处理
if os.path.isfile(case_path):
    is_replace(case_path=case_path, name=name, url=url, meth=meth, remark=remark)
# 测试用例不存在
else:
    menu(name=name, url=url, meth=meth, case_path=case_path, remark=remark)
