#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/29 18:22
# @Author : xiaomo
# @Site : 
# @File : base_api.py
# @Software: PyCharm
# coding:utf-8
import json
import requests,sys
from Interface_plus.common.readexcel import ExcelUtil
from Interface_plus.common.writeexcel import copy_excel, Write_excel
reload(sys)
sys.setdefaultencoding('utf-8')


def send_requests(s, testdata):
    '''封装requests请求'''
    method = testdata["method"]
    url = testdata["url"]
    # url后面的params参数
    try:
        params = eval(testdata["params"])
        # print type(params)
    except:
        params = None
    # 请求头部headers
    try:
        headers = eval(testdata["headers"])
        print("请求头部：%s" % headers)
    except:
        headers = None
    #代入cookie
    try:
        cookies=eval(testdata['cookies'])
    except:
        cookies=None
    # post请求body类型
    type = testdata["type"]

    test_nub = testdata['id']
    print("*******正在执行用例：-----  %s  ----**********" % test_nub)
    print("请求方式：%s, 请求url:%s" % (method, url))
    print("请求params：%s" % params)

    # post请求body内容
    try:
        bodydata = eval(testdata["body"])
    except:
         bodydata = {}

    # 判断传data数据还是json
    if type == "data":
        body = bodydata
    elif type == "json":
        body = json.dumps(bodydata,encoding="UTF-8",ensure_ascii=False)
        # body=json.loads(body).encode('utf-8')
        # body=json.loads(body)
        # print type(body)
    else:
        body = json.loads(bodydata)

    if method == "post":
        print("post请求body类型为：%s ,body内容为：%s" % (type, body))

    verify = False
    res = {}   # 接受返回数据

    try:
        r = s.request(method=method,
                      url=url,
                      params=params,
                      headers=headers,
                      data=body,
                      cookies=cookies,
                      verify=verify
                       )
        print("页面返回信息：%s" % r.content.decode("utf-8"))
        res['id'] = testdata['id']
        res['rowNum'] = testdata['rowNum']
        res["statuscode"] = str(r.status_code)  # 状态码转成str
        res["text"] = r.content.decode("utf-8")
        # print type(res["text"])
        res["times"] = str(r.elapsed.total_seconds())   # 接口请求时间转str
        if res["statuscode"] != "200":
            res["error"] = res["text"]
        else:
            res["error"] = ""
        res["msg"] = ""
        if testdata["checkpoint"] in res["text"]:
            res["result"] = "pass"
            print("用例测试结果:   %s---->%s" % (test_nub, res["result"]))
        else:
            res["result"] = "fail"
        return res
    except Exception as msg:
        res["msg"] = str(msg)
        return res

def wirte_result(result, filename="result.xlsx"):
    # 返回结果的行数row_nub
    row_nub = result['rowNum']
    # 写入statuscode
    wt = Write_excel(filename)
    wt.write(row_nub, 8, result['statuscode'])       # 写入返回状态码statuscode,第8列
    wt.write(row_nub, 9, result['times'])            # 耗时
    wt.write(row_nub, 10, result['error'])            # 状态码非200时的返回信息
    wt.write(row_nub, 12, result['result'])           # 测试结果 pass 还是fail
    wt.write(row_nub, 13, result['msg'])           # 抛异常
    # wt.write(row_nub,14,result['operate'])
if __name__ == "__main__":
    data = ExcelUtil("debug_api.xlsx").dict_data()
    # print(data[0])
    # print type(data[0])
    # print data[0]['body']
    # print type(data[0]['body'])

    s = requests.session()
    res = send_requests(s, data[0])
    copy_excel("debug_api.xlsx", "result.xlsx")
    # print res
    # print res
    # print json.dumps(res)
    print res['text']
    print type(res['text'])
    wirte_result(res, filename="result.xlsx")