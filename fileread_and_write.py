import time
f1 = open(file="baidu_x_system.txt",mode="r+",encoding="utf-8")
data = []
data1={}
for line in f1.readlines():
    line=line.strip("\n")
    line=line.split()
    data.append(line)
print(data)
while True:
    for i in range(len(data)):
        data1[data[i][0]] = 0
        for y in range(1,len(data)-1):
            if data[i][0]==data[y][0]:
                continue
            else:
                data1[data[i][0]] = 0
    for i in data1:
        for y in range(len(data)):
            if i==data[y][0]:
                data1[i]+=1
        print("用户ip为：",i,"访问了",data1[i],"次")
    time.sleep(5)