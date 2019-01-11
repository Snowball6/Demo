# -*- coding:utf-8 -*-
# Author:ChenZhipeng
# Time:2019/1/11 14:53
# https://blog.csdn.net/fanlei_lianjia/article/details/78225857
import openpyxl
wb_data = openpyxl.load_workbook("merge_test.xlsx")  # 数据表
wb_merge = openpyxl.load_workbook("merge.xlsx")    # 最终表
ws = wb_merge.get_sheet_by_name("merge")  # 操作最终表中的merge这个sheet表
op_sheet = wb_data.sheetnames
for cloumn_name in op_sheet:
    print(cloumn_name)
    