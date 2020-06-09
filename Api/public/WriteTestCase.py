#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   WriteTestCase.py
 
@Time    :   2020/5/28 1:38 下午
'''


def WriteTestCase(
        filepath: str,
        linenum: int,
        content: str
):
    '''
    向代码中追加方法
    :param name: 方法名
    :param filepath: 文件路径
    :param linenum: 行号
    :param content: 写入内容
    :return:
    '''
    lines = []
    with open(filepath, 'r', encoding='utf-8') as lf:
        for line in lf:
            lines.append(line)
    # print(lines)
    lines.insert(linenum, content)
    s = ''.join(lines)

    with open(filepath, 'w+', encoding='utf-8') as lf:
        lf.write(s)
