#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/27 15:24
# @Author : xiaomo
# @Site : 
# @File : run.py
# @Software: PyCharm
import os
import unittest,base64
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from common import HTMLTestRunnerCN
from common import readEmailConfig

# 当前脚本所在文件真实路径


curpath = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(curpath, "report")
if not os.path.exists(report_path): os.mkdir(report_path)
case_path = os.path.join(curpath, "case")

# def add_case(caseName="cases", rule="test_*.py"):
#     """第一步：加载所有测试用例"""
#     case_path = os.path.join(cur_path, caseName)  # 用例文件夹
#     # 文件夹不存在就创建一个文件夹
#     if not os.path.exists(case_path): os.mkdir(case_path)
#
#     # 定义discover加载所有测试用例
#     # case_path：执行用例的目录；pattern：匹配脚本名称的规则；top_level_dir：默认为None
#     discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
#     return discover
def add_case(casepath=case_path, rule="test*.py"):
    '''加载所有的测试用例'''
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(casepath,
                                                  pattern=rule,)

    return discover

def run_case(all_case, reportName="report"):
    """第二步：执行所有的用例，并把结果写入到html测试报告中"""
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(curpath, reportName)
    if not os.path.exists(report_path): os.mkdir(report_path)
    report_abspath = os.path.join(report_path, now + "result.html")
    print("report path:%s" % report_abspath)

    fp = open(report_abspath, "wb")
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title="自动化接口测试报告，测试结果如下：",
                                                  description="用例执行情况")
    # 调用add_case函数
    runner.run(all_case)
    fp.close()


def get_report_file(report_path):
    """第三步：获取最新的测试报告"""
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print("最新测试生成的报告：" + lists[-1])
    # 找到生成最新的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file


def send_mail(sender, psw, receiver, smtpserver, report_file, port):
    """第四步：发送最新的测试报告内容"""
    with open(report_file, "rb") as f:
        mail_body = f.read()

    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype="html", _charset="utf-8")
    msg["Subject"] = "自动化测试报告"
    msg["from"] = sender
    msg["to"] = ','.join(receiver)
    msg.attach(body)

    # 添加附件
    att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = "attachment;filename = 'report.html'"
    msg.attach(att)
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, port)

    # 用户名密码
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print("test report email has send out")


if __name__ == '__main__':


    all_case = add_case()  # 加载用例
    run_case(all_case)  # 执行用例

    report_path = os.path.join(curpath, "report")
    report_file = get_report_file(report_path)

    # 邮箱配置，邮箱信息获取
    sender = readEmailConfig.sender
    psw = readEmailConfig.psw
    psw=base64.decodestring(psw)
    # print psw
    smtp_server = readEmailConfig.smtp_server
    port = readEmailConfig.port
    receiver = readEmailConfig.receiver
    receiver = str(receiver)
    receivers = list(receiver.split(' '))
    send_mail(sender, psw, receivers, smtp_server, report_file, port)  # 调用发送邮件方法

