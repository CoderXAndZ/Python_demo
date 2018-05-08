#! /usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 创建 excel 表格

import xlwt


wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet 1')
# indexing is zero based, row then column
sheet.write(0,1,'test text')
sheet.write(1,1,'test text')
wbk.save('/Users/admin/Desktop/接口测试结果统计/test2.xls')  # 默认保存在桌面上

