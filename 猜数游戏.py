'''
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
任务：如果键盘输入大于随机数弹出友好提示信息“猜大了”，猜小了
起始金额  5000 才对一次给300 猜错扣除100
支持充值金额
当余额为0不充值时退出或自动退出
仅在猜对的情况下修改系统获取的数值
'''
'''
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断         操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环         操作完填入：while 条件循环
任务：如果键盘输入大于随机数弹出友好提示信息“猜大了”，猜小了
起始金额  5000 才对一次给300 猜错扣除100 
支持充值金额
当余额为0不充值时退出或自动退出
仅在猜对的情况下修改系统获取的数值
'''



import random
print("猜数小游戏")
Fmoney=5000
Award=300
Amercement=100
#A=0
print("=========================================")
print("             欢迎光临，祝您好运             ")
Ran=random.randint(1,20)
while True:
    print("=========================================")

    cs=int(input("请输入您想猜的数（1~20）："))
    if Ran==cs:
        print("猜对了")
        Fmoney+=Award
    else:
        if cs>Ran:
            print("猜大了")
        else:
            print("猜小了")
        Fmoney-=Amercement
    print("当前余额为：", Fmoney)
    #A+=1
    if Fmoney<=0:
        judge=input("您的余额不足，是否充值,输入是否？")
        if judge=="是":
         cz=int(input("输入金额："))
         if cz>0:
            Fmoney+=cz
            continue
        else:
            break
    """
    if A==15:
        break
        该判断为游戏仅进行15次
    """
    if Ran==cs:
        Ran = random.randint(1, 20)
    tu=input("继续游戏输入F，输入其他均退出：")
    if tu!="F":
        break


