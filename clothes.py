import xlrd
'''
from openpyxl import load_clothes
book=load_clothes(filename=r"D:\day1.xlsx")
sheet=book.get_sheet_by_name("1")
data=[]
row_num=1
while row_num<=31:
    data.append(sheet.cell(row=row_num,column=1).value)
    row_num=row_num+1
'''
data = xlrd.open_workbook('D:\day1\\12月份衣服销售数据.xls')
'''table = data.sheet_by_name(u'1')
table.row_values()
table.col_values()
table.nrows
table.ncols
table.cell(0,0).value
'''
table = data.sheet_by_index(0)
rows=table.nrows
cols=table.ncols
a=0
b=0
c=0
e=0
f=0
for i in range(1,rows):
    data=table.row_values(i)
    a+=data[2]*data[4]
    b+=data[4]
    c+=1
name=data[1]


d=b/c
print("总销售额为：",a)
print("平均每日销售数量为：",d)
'''
for i in range(1,rows):
    data=table.row_values(i)
    b+=data[4]
    c+=1
d=b/c
print(d)
'''


s=[]
t=[]
q=0
for i in range(1,rows):
    data=table.row_values(i)
    s.append(data[1])
s2=list(set(s))
for l in s:
    if l not in t:
        t.append(l)
for j in t:
    print(j,"月销售量占比为：")
    for k in range(1,rows):
        data = table.row_values(k)
        if str(data[1])==str(j):
            q+=data[4]
    print(q/b)
    q=0
#print(s)



















