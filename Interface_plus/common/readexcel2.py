#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/30 9:32
# @Author : xiaomo
# @Site : 
# @File : readexcel2.py
# @Software: PyCharm
import xlrd
import json
import pandas as pd
class ExcelUtil():
    def __init__(self, excelPath):
        self.data = pd.read_excel(excelPath)

    def dict_data(self):
        re=self.data.to_dict(orient="records")
        return re
if __name__ == "__main__":
    filepath = "test_api.xlsx"
    data = ExcelUtil(filepath)
    print data.dict_data()
    print type(data.dict_data())