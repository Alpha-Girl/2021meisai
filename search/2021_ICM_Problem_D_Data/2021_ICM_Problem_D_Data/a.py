#coding=gbk

import os
import xlrd

#������Ҫ��ȡExcel����·��
data = xlrd.open_workbook(r'full_music_data.csv')
table = data.sheets()[0]

#����һ�����б��洢Excel������
tables = []
 
 
#��excel������ݵ��뵽tables�б���
def import_excel(excel):
  for rown in range(excel.nrows):
   array = {'road_name':'','bus_plate':'','timeline':'','road_type':'','site':''}
   array['road_name'] = table.cell_value(rown,0)
   array['bus_plate'] = table.cell_value(rown,1)
   #��Excel����е�ʱ���ʽת��
   if table.cell(rown,2).ctype == 3:
     date = xldate_as_tuple(table.cell(rown,2).value,0)
     array['timeline'] = datetime.datetime(*date)
   array['road_type'] = table.cell_value(rown,3)
   array['site'] = table.cell_value(rown,4)
   tables.append(array)
