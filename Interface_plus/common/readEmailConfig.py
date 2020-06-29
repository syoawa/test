#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/27 16:33
# @Author : xiaomo
# @Site : 
# @File : readEmailConfig.py
# @Software: PyCharm
# ================读取cfg.ini文件设置=================

import os
import configparser

# os.path.realpath(__file__)：返回当前文件的绝对路径
# os.path.dirname()： 返回（）所在目录
cur_path = os.path.dirname(os.path.realpath(__file__))  # 当前文件的所在目录
configPath = os.path.join(cur_path, "email_config.ini")  # 路径拼接：/config/email_config.ini
conf = configparser.ConfigParser()
conf.read(configPath, encoding='UTF-8')  # 读取/config/email_config.ini 的内容

# get(section,option) 得到section中option的值，返回为string类型
smtp_server = conf.get("email", "smtp_server")
# print smtp_server
sender = conf.get("email", "sender")
# print sender
psw = conf.get("email", "psw")
# print psw
receiver = conf.get("email", "receiver")
receiver = str(receiver)
receivers = list(receiver.split(' '))
print(receivers)
# print type(receiver)
port = conf.getint("email", "port")


