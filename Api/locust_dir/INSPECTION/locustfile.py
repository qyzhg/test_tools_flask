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







#Tue Jun  9 10:08:43 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __login_POST_DATA(self):
        '''
        admin登录
        '''
        self.Api.api('login_POST_DATA')


#Tue Jun  9 10:09:18 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __LOGIN_POST_DATA(self):
        '''
        admin登录
        '''
        self.Api.api('LOGIN_POST_DATA')


#Tue Jun  9 17:07:49 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __inspectionManagement_inspectionPerson_asySave_POST_DATA(self):
        '''
        添加视察员
        '''
        self.Api.api('inspectionManagement_inspectionPerson_asySave_POST_DATA')


#Tue Jun  9 17:12:20 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __inspectionManagement_inspectionPerson_asySave_GET(self):
        '''
        添加视察员
        '''
        self.Api.api('inspectionManagement_inspectionPerson_asySave_GET')


#Tue Jun  9 17:13:50 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __inspectionManagement_inspectionPerson_asySave_POST_JSON(self):
        '''
        添加视察员
        '''
        self.Api.api('inspectionManagement_inspectionPerson_asySave_POST_JSON')


#Tue Jun  9 17:14:17 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __inspectionManagement_inspectionPerson_asySave_POST_JSON(self):
        '''
        添加视察员
        '''
        self.Api.api('inspectionManagement_inspectionPerson_asySave_POST_JSON')


#Tue Jun  9 17:15:12 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __inspectionManagement_inspectionPerson_asySave_POST_JSON(self):
        '''
        添加视察员
        '''
        self.Api.api('inspectionManagement_inspectionPerson_asySave_POST_JSON')


#Tue Jun  9 17:19:06 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __inspectionManagement_inspectionPerson_asySave_GET(self):
        '''
        这是备注
        '''
        self.Api.api('inspectionManagement_inspectionPerson_asySave_GET')


#Tue Jun  9 18:28:36 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __我的免费隧道(self):
        '''
        添加视察员ddd
        '''
        self.Api.api('我的免费隧道')


#Tue Jun  9 18:29:18 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __ggg(self):
        '''
        添加视察员
        '''
        self.Api.api('ggg')


#Tue Jun  9 18:34:55 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __我的免费隧道(self):
        '''
        dafdas
        '''
        self.Api.api('我的免费隧道')


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