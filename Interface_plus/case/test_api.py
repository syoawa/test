#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/29 18:32
# @Author : xiaomo
# @Site : 
# @File : test_api.py
# @Software: PyCharm
# coding:utf-8
import unittest
import ddt
import os
import requests
from Interface_plus.common import Get_Session
import json
from Interface_plus.common import base_api
from Interface_plus.common import readexcel
from Interface_plus.common import writeexcel


# 获取demo_api.xlsx路径
curpath = os.path.dirname(os.path.realpath(__file__))
print (curpath)
testxlsx = os.path.join(curpath, "test_api.xlsx")

# 复制test_api.xlsx文件到xlsx_results下
report_path = os.path.join(os.path.dirname(curpath), "report")
resultxlsx_path=os.path.join(os.path.dirname(curpath),"xlsx_results")
reportxlsx = os.path.join(resultxlsx_path, "result.xlsx")
#使用cookie，在excel中写入cookie
c=Get_Session.getCookie()
cookie=c.get_cookie("ivil","123456789")
# cookie=c.get_cookie("xm5","xiaomo123")
wr=writeexcel.Write_excel(testxlsx)
for i in range(44):
    wr.write(i+2,15,json.dumps({"ticket":cookie}))

testdata = readexcel.ExcelUtil(testxlsx).dict_data()
@ddt.ddt
class Test_api(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        writeexcel.copy_excel(testxlsx, reportxlsx) # 复制xlsx

    @ddt.data(*testdata)
    def test_api(self, data):
        # 先复制excel数据到report
        res = base_api.send_requests(self.s, data)

        base_api.wirte_result(res, filename=reportxlsx)
        # 检查点 checkpoint
        check = data["checkpoint"]
        print("检查点->：%s"%check)
        # 返回结果
        res_text = res["text"]
        print("返回实际结果->：%s"%res_text)
        # 断言
        self.assertTrue(check in res_text)

if __name__ == "__main__":
    unittest.main()