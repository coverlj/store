import time
f1=open(file="baidu_x_system.log",mode="r+",encoding="utf-8")
f2=open(file="d:\\rzgx.txt",mode="w+",encoding="utf-8")
data=[]
data1={}
for line in f1.readlines():
    line=line.strip("\n")
    line=line.split()
    data.append(line)
while True:
    for i in range(len(data)):
        data1[data[i][0]] = 0
    for i in data1:
        for y in range(len(data)):
            if i==data[y][0]:
                data1[i]+=1
        f2.write("用户ip是：")
        f2.write(i)
        f2.write("\n访问次数是：")
        f2.write(str(data1[i]))
        f2.write("\n")
    time.sleep(30)