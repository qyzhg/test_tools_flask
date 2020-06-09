#!/usr/bin/env python

# -*- encoding: utf-8 -*-

#该文件由程序自动生成，请检查后使用


import sys
import unittest
import os
import warnings

try:
    import requests
except ImportError:
    print('发现缺少的依赖库，正在尝试安装，如果安装失败，请使用pip install requests命令自行安装')
    os.system('pip install requests')
    import requests
sys.path.append(os.path.dirname
                (os.path.dirname
                 (os.path.dirname
                  (os.path.dirname
                   (os.path.abspath(__file__))))))
from Api.public.API import Api

class test_api(unittest.TestCase, Api):
    def setUp(self) -> None:
        warnings.simplefilter('ignore',ResourceWarning)
        self.s = requests.Session()
        # self.login()

