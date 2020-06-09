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

#Tue Jun  9 10:08:43 2020该代码由工具自动生成，请检查后使用！
    def test_login_POST_DATA(self):
        '''
        admin登录
        '''
        r = self.api('login_POST_DATA')

#Tue Jun  9 10:09:18 2020该代码由工具自动生成，请检查后使用！
    def test_LOGIN_POST_DATA(self):
        '''
        admin登录
        '''
        r = self.api('LOGIN_POST_DATA')

#Tue Jun  9 10:10:44 2020该代码由工具自动生成，请检查后使用！
    def test_LOGIN_POST_DATA(self):
        '''
        
        '''
        r = self.api('LOGIN_POST_DATA')

#Tue Jun  9 17:07:49 2020该代码由工具自动生成，请检查后使用！
    def test_inspectionManagement_inspectionPerson_asySave_POST_DATA(self):
        '''
        添加视察员
        '''
        r = self.api('inspectionManagement_inspectionPerson_asySave_POST_DATA')

#Tue Jun  9 17:12:20 2020该代码由工具自动生成，请检查后使用！
    def test_inspectionManagement_inspectionPerson_asySave_GET(self):
        '''
        添加视察员
        '''
        r = self.api('inspectionManagement_inspectionPerson_asySave_GET')

#Tue Jun  9 17:13:50 2020该代码由工具自动生成，请检查后使用！
    def test_inspectionManagement_inspectionPerson_asySave_POST_JSON(self):
        '''
        添加视察员
        '''
        r = self.api('inspectionManagement_inspectionPerson_asySave_POST_JSON')

#Tue Jun  9 17:14:17 2020该代码由工具自动生成，请检查后使用！
    def test_inspectionManagement_inspectionPerson_asySave_POST_JSON(self):
        '''
        添加视察员
        '''
        r = self.api('inspectionManagement_inspectionPerson_asySave_POST_JSON')

#Tue Jun  9 17:15:12 2020该代码由工具自动生成，请检查后使用！
    def test_inspectionManagement_inspectionPerson_asySave_POST_JSON(self):
        '''
        添加视察员
        '''
        r = self.api('inspectionManagement_inspectionPerson_asySave_POST_JSON')

#Tue Jun  9 17:19:06 2020该代码由工具自动生成，请检查后使用！
    def test_inspectionManagement_inspectionPerson_asySave_GET(self):
        '''
        这是备注
        '''
        r = self.api('inspectionManagement_inspectionPerson_asySave_GET')

#Tue Jun  9 18:28:36 2020该代码由工具自动生成，请检查后使用！
    def test_我的免费隧道(self):
        '''
        添加视察员ddd
        '''
        r = self.api('我的免费隧道')

#Tue Jun  9 18:29:18 2020该代码由工具自动生成，请检查后使用！
    def test_ggg(self):
        '''
        添加视察员
        '''
        r = self.api('ggg')

#Tue Jun  9 18:34:55 2020该代码由工具自动生成，请检查后使用！
    def test_我的免费隧道(self):
        '''
        dafdas
        '''
        r = self.api('我的免费隧道')

