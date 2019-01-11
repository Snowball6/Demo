# -*- coding:utf-8 -*-
# Author:ChenZhipeng
# Time:2019/1/11 14:53

# https://openpyxl.readthedocs.io/en/stable/tutorial.html

import openpyxl
wb_total = openpyxl.Workbook("Jan_upper.xlsx")  # 新建工作薄
wb_data = openpyxl.load_workbook('data.xlsx')  # 打开需要分析的工作薄
ws = wb_total.create_sheet("merge")         # 新建sheet
ws.sheet_properties.tabColor = "1072BA"     # 给sheet表添加颜色
op_sheet = wb_data.sheetnames   # 获取分析的工作薄中的sheet名
for sheet in wb_data:
    print(sheet.title)




#wb_total.save("Jan_upper.xlsx")