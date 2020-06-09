#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   send_mail.py
 
@Time    :   2019/12/29 1:10 下午
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

host='smtp.163.com' #发件服务器地址
user='qyzhg@163.com' #发送邮件用户
pwd='qyzhg876407' #密码
milelist='442991457@qq.com' #收件人邮箱，如果多个邮箱字符串中间用逗号隔开
text="邮件正文"   #邮件正文
Subject="邮件主题" #邮件主题
file=("./report/2019-12-28 22_14_10_reportCN.html")#附件

class Email(object):
    """
    a=Email(host,user,pwd,milelist,text,Subject) #创建对象
    a.send_text()  #如果只发送正文，调用该方法
    a.send_file(file) #如果正文+附件，调用该方法需要传入file附件元祖形式入参，多个文件地址用逗号隔开
    a.send() #发送邮件

    """
    def __init__(self,host=host,user=user,pwd=pwd,milelist=milelist,text=text,Subject=Subject):
        self.host = host #发件服务器地址
        self.user = user #发件人邮箱
        self.pwd = pwd #发件人密码
        self.milelist = milelist #收件人邮箱，如果多个字符串邮箱之间用逗号隔开
        self.text = text  #邮件正文
        self.Subject = Subject #邮件主题

    def send_text(self):
        if "qq" in milelist:
            self.msg = MIMEText(self.text)
        else:
            self.msg = MIMEText(self.text, 'utf-8')  # 执行utf-8编码
            self.msg["Accept-Language"] = "zh-CN"  # 添加两个属性
            self.msg["Accept-Charset"] = "ISO-8859-1,utf-8"
        self.msg["Subject"]=self.Subject
        self.msg["From"]=self.user
        self.msg["To"]=self.milelist

    def send_file(self,file):
        '''
        file:字典形式入参，key：文件的绝对路径，values：文件名称
        '''
        self.msg = MIMEMultipart()
        self.msg["Subject"] = self.Subject
        self.msg["From"] = self.user
        self.msg["To"] = self.milelist
        try:
            att = MIMEText(open(file, 'rb').read(), 'base64', 'gb2312')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename="' + file.split("/")[-1] + '"'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        except Exception as e:
            print("附件的文件路径错误：",e)
        else:
            self.msg.attach(att)
        #有些邮箱正文会乱码，需要指定为utf-8编码然后再添加两个属性，但是有些邮箱不支持该方法，添加后正文会变为空
        #所以要条件判断一下，下例是qq邮箱不支持，所以判断一下，如果是qq邮箱，就不用指定utf8
        if "qq" in milelist:
            self.msg.attach(MIMEText(self.text))
        else:
            self.msg.attach(MIMEText(self.text, 'utf-8'))  #执行utf-8编码
            self.msg["Accept-Language"] = "zh-CN"  #添加两个属性
            self.msg["Accept-Charset"] = "ISO-8859-1,utf-8"

    def send(self):
        try:
            self.smtp=smtplib.SMTP(self.host,port=25)  #连接邮件服务器，传入发件服务器地址和端口号
        except Exception as e:
            print("无法连接邮件服务器",e)
        else:
            try:
                self.smtp.login(self.user,self.pwd)  #登陆发件人邮箱，传入邮箱地址和密码
            except Exception as e:
                print("发件人邮箱登陆失败：",e)
            else:
                self.smtp.sendmail(self.user,self.milelist.split(','),self.msg.as_string()) #发送邮件，参数分别是发件人、收件人、发件内容变成字符串
        finally:
            self.smtp.quit() #关闭发件服务器连接

if __name__ == '__main__':
    a = Email(host, user, pwd, milelist, text, Subject)  # 创建对象
    # a.send_text()  # 如果只发送正文，调用该方法
    a.send_file(file)  # 如果正文+附件，调用该方法需要传入file附件元祖形式入参，多个文件地址用逗号隔开
    a.send()  # 发送邮件