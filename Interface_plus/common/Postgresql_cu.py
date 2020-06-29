#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/21/0021 14:16
# @Author : xiaomo
# @File : Postgresql_cu.py
# @Software: PyCharm
# from  psycopg2 import connect
# import os
# import configparser
# #========读取db_config.ini文件设置==========
# cur_path = os.path.dirname(os.path.realpath(__file__))
# configPath = os.path.join(cur_path, "db_config.ini")
# cf = configparser.ConfigParser()
# cf.read(configPath, encoding='UTF-8')
# host = cf.get("PostgreSQLconf", "host")
# port = cf.get("PostgreSQLconf", "port")
# db = cf.get("PostgreSQLconf", "db_name")
# user = cf.get("PostgreSQLconf", "user")
# password = cf.get("PostgreSQLconf", "password")
#
#
# # ================封装PostgreSQL基本操作=================
# class DB(object):
#     def __init__(self):
#         # 连接数据库
#         self.conn = connect(
#             "dbname={} user={} password={} port={} host={}".format(db,user,password,port,host)
#             )
#
#     # 清除表数据
#     def clear(self, tabel_name):
#         real_sql = "delete from " + tabel_name + ";"
#         with self.conn.cursor() as cursor:
#             cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
#             cursor.execute(real_sql)
#         self.conn.commit()
#
#     # 插入表数据
#     def insert(self, table_name, table_data):
#         for key in table_data:
#             table_data[key] = "'" + str(table_data[key]) + "'"
#         key = ','.join(table_data.keys())
#         value = ",".join(table_data.values())
#         real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")" + ";"
#         print(real_sql)
#         with self.conn.cursor() as cursor:
#             cursor.execute(real_sql)
#         self.conn.commit()
#
#     # 关闭数据库连接
#     def close(self):
#         self.conn.close()
#
#
# if __name__ == '__main__':
#     db = DB()
#     table_name = ""
#     data = {
#             }
#     db.clear(table_name)
#     db.insert(table_name, data)
#     db.close()
