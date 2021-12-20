import xlrd2
import pandas as pd
from xlutils.copy import copy
# import numpy
class dq:
    def xlrd_excel(self,textdata,a):
        # data = xlrd2.open_workbook(filename=r"计算器数据.xlsx", encoding_override=True)
        data = xlrd2.open_workbook(filename=textdata, encoding_override=True)
        tables = data.sheet_by_index(0)
        row = tables.nrows
        datasj=[]
        datasj1=[]
        for i in range(1,row):
            for y in range(0,a):
                datasj.append(tables.cell(i,y).value)
        for i in range(0,len(datasj)//a):
            for y in range(0,a):
              if y==0:
                  datasj1.append([])
              datasj1[i].append(datasj[y+i*a])
        return datasj1
    def xlwt_excel(self,a,b,c,textdata):
        new_excel= copy(xlrd2.open_workbook(filename=textdata, encoding_override="utf-8"))
        getrow=pd.read_excel(textdata)
        for indexs in getrow.index:
            for i in range(len(getrow.loc[indexs].values)):
                if (getrow.loc[indexs].values[i]==a):
                    ws = new_excel.get_sheet(0)
                    ws.write(indexs+1,c,b)
                    new_excel.save(textdata)
            print(a,b,textdata)
#测试从exc表中获取数据源
# t = dq()
# print(t.xlrd_excel("d:/工商银行数据测试报告.xls",8))
# a=[1,2,3,4,5,6,7,8,9,1,2,3]
# b=numpy.array(a).reshape(3,4) # reshape(列的长度，行的长度)
# print(b)
#测试向Excel表中指定单元格输入内容
# ss=dq()
# ss.xlwt_excel("鲁晶1","成功","d:/工商银行数据测试报告.xls")
# a=[1,2,3,4,5,6,7,8,9,1,2,3]
# b=[]
# for i in range(0,4):#分为几个二维列表
#     for y in range(0,3):#每个二维列表中的数的数量
#         if y==0:
#             b.append([])
#         b[i].append(a[y+i*3])
# print(b)






