#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   start.py
 
@Time    :   2020/6/2 8:51 上午
'''

import os
import sys
from shutil import copyfile

from Api.settings import PARENT_LOCUSTFILE_DIR, PARENT_CASE_DIR, PARENT_TEST_API_DIR, PARENT_REPORT_DIR ,TEMPLATE_DIR


def start_project(startname):
    if not os.path.isdir(PARENT_CASE_DIR):
        #创建测试用例目录
        os.makedirs(PARENT_CASE_DIR)
    if not os.path.isdir(PARENT_TEST_API_DIR):
        #创建接口测试脚本目录
        os.makedirs(PARENT_TEST_API_DIR)
    if not os.path.isdir(PARENT_LOCUSTFILE_DIR):
        #创建性能测试脚本目录
        os.makedirs(PARENT_LOCUSTFILE_DIR)
    if not os.path.isdir(PARENT_REPORT_DIR):
        #创建测试报告目录
        os.makedirs(PARENT_REPORT_DIR)

    start = startname.upper()
    locust_dir, test_api_dir, case_dir ,report_dir= (
                                                        os.path.join(PARENT_LOCUSTFILE_DIR, start)), (
                                                        os.path.join(PARENT_TEST_API_DIR, 'test_'+start)), (
                                                        os.path.join(PARENT_CASE_DIR, start)),(
                                                        os.path.join(PARENT_REPORT_DIR,start))
    make_locust_dir(locust_dir)
    make_test_api_dir(test_api_dir)
    make_case_dir(case_dir)
    make_report_dir(report_dir)
    sys.exit(0)


def make_locust_dir(locust_dir):
    if os.path.isdir(locust_dir):
        print('新建locust项目失败！\n{locust_dir}目录已存在，请检查路径！'.format(locust_dir=locust_dir))
    else:
        # 新建locust项目目录
        os.makedirs(locust_dir)
        print('新建locust目录成功!\n{locust_dir}\n'.format(locust_dir=locust_dir))
        make_locust_files(locust_dir)


def make_test_api_dir(test_api_dir):
    if os.path.isdir(test_api_dir):
        print('新建test_api项目失败！\n{test_api_dir}目录已存在，请检查路径！'.format(test_api_dir=test_api_dir))
    else:
        # 新建test_api项目目录
        os.makedirs(test_api_dir)
        print('新建test_api目录成功!\n{test_api_dir}\n'.format(test_api_dir=test_api_dir))
        make_test_api_files(test_api_dir)


def make_case_dir(case_dir):
    if os.path.isdir(case_dir):
        print('新建case_dir项目失败！\n{case_dir}目录已存在，请检查路径！'.format(case_dir=case_dir))
    else:
        # 新建case_dir项目目录
        os.makedirs(case_dir)
        print('新建case_dir目录成功!\n{case_dir}\n'.format(
            case_dir=case_dir))

def make_report_dir(report_dir):
    if os.path.isdir(report_dir):
        print(f'新建report_dir项目失败！\n{report_dir}目录已存在，请检查路径！')
    else:
        # 新建report_dir项目目录
        os.makedirs(report_dir)
        print(f'新建report_dir目录成功!\n{report_dir}\n')


def make_locust_files(locust_dir):
    old_init_file = os.path.join(TEMPLATE_DIR, '__init__.py')
    new_init_file = os.path.join(locust_dir, '__init__.py')
    copyfile(old_init_file, new_init_file)
    print('在{locust_dir}中生成初始化文件成功！'.format(locust_dir=locust_dir))
    old_locust_file = os.path.join(TEMPLATE_DIR, 'locustfile.py')
    new_locust_file = os.path.join(locust_dir, 'locustfile.py')
    copyfile(old_locust_file, new_locust_file)
    print('在{locust_dir}中生成locustfile文件成功！'.format(locust_dir=locust_dir))


def make_test_api_files(test_api_dir):
    old_init_file = os.path.join(TEMPLATE_DIR, '__init__.py')
    new_init_file = os.path.join(test_api_dir, '__init__.py')
    copyfile(old_init_file, new_init_file)
    print('在{test_api_dir}中生成初始化文件成功！'.format(test_api_dir=test_api_dir))
    old_test_api = os.path.join(TEMPLATE_DIR, 'test_api.py')
    new_test_api = os.path.join(test_api_dir, 'test_api.py')
    copyfile(old_test_api, new_test_api)
    print('在{test_api_dir}中生成test_api文件成功！'.format(test_api_dir=test_api_dir))
