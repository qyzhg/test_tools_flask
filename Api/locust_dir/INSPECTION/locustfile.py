#!/usr/bin/env python

# -*- encoding: utf-8 -*-

#该文件由程序自动生成，请检查后使用


import os,sys
sys.path.append(os.path.dirname
                (os.path.dirname
                 (os.path.dirname
                  (os.path.dirname
                   (os.path.abspath(__file__))))))
from Api.public.API import Api


import gevent
from locust import HttpUser, task, between
from locust.env import Environment
from locust.stats import stats_printer
from locust.log import setup_logging

setup_logging("INFO", None)


class User(HttpUser):
    wait_time = between(1, 3)
    host = ""

    def on_start(self):
        self.s = self.client
        self.Api = Api(self.s)








#Tue Jun  9 22:54:25 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __测试名称(self):
        '''
        哈哈
        '''
        self.Api.api('测试名称')


#Tue Jun  9 22:54:25 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __测试名称(self):
        '''
        哈哈
        '''
        self.Api.api('测试名称')


#Tue Jun  9 22:56:28 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __测试名称(self):
        '''
        哈哈
        '''
        self.Api.api('测试名称')


#Tue Jun  9 22:56:28 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __(self):
        '''
        
        '''
        self.Api.api('')


#Tue Jun  9 22:57:13 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __测试名称(self):
        '''
        哈哈
        '''
        self.Api.api('测试名称')


#Tue Jun  9 23:24:11 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __(self):
        '''
        
        '''
        self.Api.api('')


#Tue Jun  9 23:29:50 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __(self):
        '''
        
        '''
        self.Api.api('')


#Tue Jun  9 23:29:50 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __(self):
        '''
        
        '''
        self.Api.api('')


#Tue Jun  9 23:29:50 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __(self):
        '''
        
        '''
        self.Api.api('')


#Tue Jun  9 23:29:50 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __(self):
        '''
        
        '''
        self.Api.api('')


#Tue Jun  9 23:29:50 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __(self):
        '''
        
        '''
        self.Api.api('')


#Tue Jun  9 23:29:50 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __(self):
        '''
        
        '''
        self.Api.api('')


#Tue Jun  9 23:29:50 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __(self):
        '''
        
        '''
        self.Api.api('')


#Tue Jun  9 23:29:50 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __(self):
        '''
        
        '''
        self.Api.api('')


#Tue Jun  9 23:29:50 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __(self):
        '''
        
        '''
        self.Api.api('')


#Tue Jun  9 23:29:50 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __(self):
        '''
        
        '''
        self.Api.api('')


#Tue Jun  9 23:29:50 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __(self):
        '''
        
        '''
        self.Api.api('')


#Tue Jun  9 23:29:50 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __(self):
        '''
        
        '''
        self.Api.api('')


#Tue Jun  9 23:29:50 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __(self):
        '''
        
        '''
        self.Api.api('')


#Tue Jun  9 23:29:50 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __(self):
        '''
        
        '''
        self.Api.api('')


#Tue Jun  9 23:59:31 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __(self):
        '''
        
        '''
        self.Api.api('')


#Tue Jun  9 23:59:31 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __(self):
        '''
        
        '''
        self.Api.api('')


# 设置环境
env = Environment(user_classes=[User])
env.create_local_runner()

# 浏览器地址
env.create_web_ui("127.0.0.1", 8089)

# 命令行定时刷新
# gevent.spawn(stats_printer(env.stats))

# 直接在命令行启动
# env.runner.start(1, hatch_rate=10)

# 定时器（秒）
gevent.spawn_later(3600, lambda: env.runner.quit())

# 集合点
env.runner.greenlet.join()

# 停止web
env.web_ui.stop()