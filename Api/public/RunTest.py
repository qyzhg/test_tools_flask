#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao

@Contact :   qyzhg@163.com

@File    :   allTestCN.py

@Time    :   2019/9/28 12:36
'''

import os
import time
import unittest
from Api.public import HTMLTestReportCN
from Api.public.send_mail import Email
from Api.settings import REPORT_DIR,TEST_API_DIR,EMAIL_ADDRESS,PROJECT_NAME,LOCUSTFILE_FILE

def runAPITEST(a:str):
    if a.upper() == PROJECT_NAME:
        runtest()
    else:
        print('输入项目名与配置项目名不符，请检查输入的项目名和settings文件')

def runLOCUST(a:str):
    if a.upper() == PROJECT_NAME:
        print('压力服务已启动，请访问 127.0.0.1:8089 进行测试')
        os.system(f'python {LOCUSTFILE_FILE}')
    else:
        print('输入项目名与配置项目名不符，请检查输入的项目名和settings文件')


def runtest():
    '''
    运行方法
    '''
    #生成报告
    fileName=os.path.join(REPORT_DIR,getNowTime()+'_reportCN.html')
    fp = open(fileName , 'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='自动化测试报告',
        description='详细信息：'
    )
    runner.run(allTests())
    print('测试报告成功生成！！',fileName)
    title = time.ctime() + '测试报告'
    #发送邮件
    mail = Email(
              #收件人
              milelist= get_accessees(),
              text = '本邮件由服务器自动发送\n'
                     +'脚本执行时间：'+time.ctime()+'\n'
                     '请将附件下载后打开，预览会出现错误\n'
                     '如果不是我公司相关研发及测试人员，联系qyzhg@163.com取消此邮件', #内容
              Subject = title )     #标题
    # 创建对象
    # a.send_text()  # 如果只发送正文，调用该方法
    mail.send_file(fileName)  # 如果正文+附件，调用该方法需要传入file路径
    print(f'是否发送邮件通知？\n收件人可以在{EMAIL_ADDRESS}文件中配置\nY:发送（默认）\nN:不发送')
    while True:
        if (a:= input('请选择:\n').upper()) == 'Y' or a == '':
            mail.send()  # 发送邮件
            print('邮件发送成功！！'+ get_accessees())
            return
        elif a == 'N':
            print('已取消！')
            return
        else:
            print('输入有误，请重新选择！')


def allTests():
    '''获取所有测试用例'''
    suite = unittest.defaultTestLoader.discover(
        start_dir=TEST_API_DIR,
        pattern='test_*.py',
        top_level_dir=None)
    return suite

def getNowTime():
    '''获取当前的时间'''
    return time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))

def get_accessees():
    '''收件人'''
    accessee_str = ''
    with open(EMAIL_ADDRESS, 'r',encoding='utf-8') as f:
        accessee_list = (f.readlines())
        for line in (accessee_list[1:]):
            line_list = line.split(',')
            if line_list[0] != '' and '启用' in line_list[3]:
                accessee_str += (line_list[0])+','
        return accessee_str[:-1]
