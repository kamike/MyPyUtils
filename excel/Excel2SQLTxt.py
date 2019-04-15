#!/usr/bin/env python
# -*- coding:utf8 -*-
# import openpyxl
# from openpyxl import load_workbook
import xlrd
# 根据excel里面的SN号列表，截取sql

workbook = xlrd.open_workbook("E:/tms_dir/1111.xls")
sheel = workbook.sheets()[0]
sql = ""
index = 0

subStr = "' or machineId='"

for row in range(sheel.nrows):
    if row <= 1:
        continue

    # colKey = sheel.cell(row=i, column=3).value
    colKey = sheel.row_values(row)[0]
    sql += colKey + subStr
    index += 1

sql = sql[0: len(sql) - len(subStr)+1]
print("UPDATE t_bd_terminal set useridalias='1.7' WHERE machineId='" + sql)  # 打印结果
print(str(index))
