import xlrd2
import pandas as pd
from xlutils.copy import copy
class dxwj():
    def xlrd_excel(self,textdata,a):
        data = xlrd2.open_workbook(filename=textdata, encoding_override=True)
        tables = data.sheet_by_index(0)
        row = tables.nrows
        datasj = []
        datasj1 = []
        for i in range(1, row):
            for y in range(0, a):
                datasj.append(tables.cell(i, y).value)
        for i in range(0, len(datasj) // a):
            for y in range(0, a):
                if y == 0:
                    datasj1.append([])
                datasj1[i].append(datasj[y + i * a])
        for i in range(len(datasj1)):
            for y in range(len(datasj1[i])):
                if type(datasj1[i][y]) == float:
                    a = datasj1[i][y]
                    datasj1[i].remove(datasj1[i][y])
                    datasj1[i].insert(y, int(a))
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
#
# t = dxwj()
# # b=t.xlrd_excel("d:/HKR.xls",4)
# # print(b)
# # for i in range(len(b)):
# #     for y in range(len(b[i])):
# #          if type(b[i][y])==float:
# #              a=b[i][y]
# #              b[i].remove(b[i][y])
# #              b[i].insert(y,int(a))
# #
# # t.xlwt_excel("admin1","成功",3,"d:/HKR.xls")
#
#
# print(t.xlrd_excel("d:/HKRsctx.xls",4))












