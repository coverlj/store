import xlrd
data = xlrd.open_workbook('D:\day1\\12月份衣服销售数据.xls')
table = data.sheet_by_index(0)
rows=table.nrows
cols=table.ncols
a=0
b=0
c=0
for i in range(1,rows):
    data=table.row_values(i)
    a+=data[2]*data[4]
    b+=data[4]
    c+=1
name=data[1]
d=b/c
print("1.1总销售额为：",a)
print("1.2平均每日销售数量为：",d)
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
print("1.3种类月销售量占比(百分比)：")
for j in t:
    print(j,"月销售量占比为：")
    for k in range(1,rows):
        data = table.row_values(k)
        if str(data[1])==str(j):
            q+=data[4]
    print(q/b)
    q=0



















