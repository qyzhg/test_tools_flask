#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   settings.py
 
@Time    :   2020/5/28 8:50 上午
'''

import os

# 此处配置项目名称.
PROJECE = 'test'

# 此处配置项目路径
HOST = 'http://10.102.111.117:8093/HCLCNNC/a/'

PROJECT_NAME = PROJECE.upper()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_CASE_DIR = os.path.join(BASE_DIR, 'case_dir')

CASE_DIR = os.path.join(PARENT_CASE_DIR, PROJECT_NAME)

PARENT_LOCUSTFILE_DIR = os.path.join(BASE_DIR, 'locust_dir')

LOCUSTFILE_DIR = os.path.join(PARENT_LOCUSTFILE_DIR, PROJECT_NAME)

LOCUSTFILE_FILE = os.path.join(LOCUSTFILE_DIR, 'locustfile.py')

PARENT_TEST_API_DIR = os.path.join(BASE_DIR, 'test_api_dir')

TEST_API_DIR = os.path.join(PARENT_TEST_API_DIR, 'test_'+PROJECT_NAME)

TEST_API_FILE = os.path.join(TEST_API_DIR, 'test_api.py')

PARENT_REPORT_DIR = os.path.join(BASE_DIR, 'report_dir')

REPORT_DIR = os.path.join(PARENT_REPORT_DIR, PROJECT_NAME)

JSON_FILE = os.path.join(BASE_DIR, 'getyaml', 'json')

TEMPLATE_DIR = os.path.join(BASE_DIR, 'public', 'template')

EMAIL_ADDRESS = os.path.join(BASE_DIR,'public','EmailAddress.csv')