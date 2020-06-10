#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   msg.py
 
@Time    :   2020/6/10 1:58 下午
'''


def Msg(a):
    msg = list()
    warning = list()
    danger = list()
    for _ in a:
        if _.get('0'):
            msg.append(_.get('0'))
        if _.get('1'):
            warning.append(_.get('1'))
        if _.get('2'):
            danger.append(_.get('2'))

    context = {
        'msg': msg,
        'warning': warning,
        'danger':danger,
    }
    return context
