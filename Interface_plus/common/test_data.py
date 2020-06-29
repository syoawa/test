#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/21/0021 16:13
# @Author : xiaomo
# @File : test_data.py
# @Software: PyCharm
import sys
sys.path.append('../db_fixture')
from Postgresql_cu import DB
datas={
    #用户表数据
    'users':[{
	"cardId": "1234",
	"createName": "xiaomo",
	"createTime": "",
	"email": "x@x",
	"gender": 0,
	"id": "",
	"imgUrl": "",
	"loginName": "xiaomo",
	"loginPwd": "xiaomo123",
	"orgId": "",
	"orgIdList": [],
	"periodate": "",
	"phoneNum": "",
	"policeId": "",
	"roleIdList": [],
	"userLevel": 0,
	"userName": ""
},{
	"cardId": "4567",
	"createName": "",
	"createTime": "",
	"email": "m@m",
	"gender": 0,
	"id": "",
	"imgUrl": "",
	"loginName": "xm_test",
	"loginPwd": "xiaomo123",
	"orgId": "",
	"orgIdList": [],
	"periodate": "",
	"phoneNum": "",
	"policeId": "",
	"roleIdList": [],
	"userLevel": 0,
	"userName": ""
}]

}
def init_data():
    db=DB()
    for table,data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table,d)
    db.close()