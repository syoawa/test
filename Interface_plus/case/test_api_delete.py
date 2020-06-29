#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/25/0025 17:23
# @Author : xiaomo
# @File : test_api_delete.py
# @Software: PyCharm
import unittest
import ddt
import os
import requests
from Interface_plus.common import Get_Session
import json
c=Get_Session.getCookie()
cookie=c.get_cookie("ivil","123456789")
class Test_Api_Delete(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://172.16.90.179:9000'
    def tearDown(self):
        print("")

    """删除接口调用"""
    def test_sql_success(self):
        '''存在该用户'''
        header={"Content-Type":"application/x-www-form-urlencoded","token":"98d71a0c6fff9051","username":"sjtest","serviceType":"datasource","serviceName":"t_srv_dru_mdata_bt_app_bt"}
        p = json.dumps({
        })
        r = requests.delete(self.base_url, data=p,headers=header)
        self.result = r.headers
        self.assertEqual(self.result["reason"], "ok")
        self.assertEqual(self.result["code"],200)


