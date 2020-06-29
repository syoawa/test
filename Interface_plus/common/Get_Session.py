#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/6/26/0026 14:51
# @Author : xiaomo
# @File : Get_Session.py
# @Software: PyCharm
import requests,json
url="http://172.16.90.233:9090"
base_url="/np-zhsq-user-service/system/login"
# door_url="/np-zhsq-base-service/access/getEntranceList"
class GetCookie(object):
    def get_cookie(self,account,password):
        self.url=url+base_url
        self.par={"password": password,
    "account": account }
        self.r=requests.post(self.url,data=json.dumps(self.par),headers={"Content-Type": "application/json"})
        # self.r=self.r.json()
        # self.s=self.r.cookies
        return self.r.cookies
if __name__=="__main__":
    co=GetCookie()
    r=co.get_cookie("admin","f64efc94f0f50c44af1ec7bf859195cd")
    print (r)
#
# class GetSession(object):
#     def get_session(self,account,password):
#         self.url=url+base_url
#         self.par={"password": password,"account": account}
#         self.s=requests.Session()
#         self.s1=self.s.post(url=self.url,data=json.dumps(self.par),headers={"Content-Type":"application/json"})
#         return self.s1.headers
# if __name__=="__main__":
#     test=GetSession()
#     s=test.get_session("admin","f64efc94f0f50c44af1ec7bf859195cd")
#     print(s)
# headers={ 'Content-Type': 'application/json'}
# s=requests.post(url=url+base_url,headers=headers,data=json.dumps({"account":"admin","password":"f64efc94f0f50c44af1ec7bf859195cd"}))
# print(s.cookies)
# data={"pageNum": 1,
# "pageSize": 12,
# "villageCode": "",
# "startTime": "",
# "endTime": "",
# "text": "",
# "sortField": "openTime",
# "sortMode": "desc"}
# r=requests.post(url=url+door_url,data=json.dumps(data),headers=headers,cookies=s.cookies)
# print(r.content)