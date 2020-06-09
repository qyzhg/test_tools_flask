#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   API.py
 
@Time    :   2020/5/27 2:51 下午
'''
try:
    import yaml
except ImportError:
    print('发现缺少的依赖库，正在尝试安装，如果安装失败，请使用pip install pyyaml命令自行安装')
    import os

    os.system('pip install pyyaml')
    import yaml
from Api.settings import *


class Api(object):
    def __init__(self, session):
        '''
        初始化方法
        :param session: requests.Session()
        '''
        self.s = session

    def api(self, case_name):
        if case_name[-5:].upper() != '.YAML':
            file_name = case_name + '.yaml'
        else:
            file_name = case_name
        # print(file_name)
        try:
            with open(os.path.join(CASE_DIR, file_name), 'r', encoding='utf-8') as f:
                y = yaml.load(f.read(), Loader=yaml.FullLoader)
        except FileNotFoundError:
            print(f'未在{CASE_DIR}找到文件{file_name}，请检查配置文件中的项目名和case文件夹中的测试用例')
            return
        # 获取yaml文件的参数
        url = HOST + y.get('url')  # 请求地址
        params = y.get('params')  # 请求参数
        name = y.get('name')  # 接口名
        meth = y.get('meth').upper()  # 获取请求方式并强转为纯大写
        if 'DATA' in meth:
            r = self.post_data(url=url, params=params)
            return r
        elif 'JSON' in meth:
            r = self.post_json(url=url, params=params)
            return r
        elif 'GET' in meth:
            r = self.get_params(url=url, params=params)
            return r
        else:
            print('{name}接口meth参数配置有误'.format(name=name))

    def post_data(self, url, params):
        r = self.s.post(url=url, data=params)
        return r

    def post_json(self, url, params):
        r = self.s.post(url=url, json=params)
        return r

    def get_params(self, url, params):
        r = self.s.get(url=url, params=params)
        return r
