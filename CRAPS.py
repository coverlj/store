import random
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("          欢迎光临花旗骰游戏        ")
import random
Fmoney=1000
print("=========================================")
print("             欢迎光临，祝您好运             ")
while True:
    ante=int(input("请输入下注金额："))
    while True:
        if ante>Fmoney:
            print("您的本金为：",Fmoney)
            print("您下的注超出您的本金！请重新输入")
            ante = int(input("请重新输入下注金额："))
        else:
            break
    Ran1=random.randint(1,6)
    print("玩家摇出了",Ran1,"点")
    Ran2=random.randint(1,6)
    print("玩家摇出了",Ran2,"点")
    Ran3=Ran1+Ran2
    while True:
        print("=========================================")
        if Ran3==7:
            print("玩家胜")
            Fmoney+=ante
            print("您的余额为：",Fmoney)
            break
        else:
            if Ran3==11:
                print("玩家胜")
                Fmoney += ante
                print("您的余额为：",Fmoney)
                break
            else:
                if Ran3==2:
                    print("庄家胜")
                    Fmoney-=ante
                    print("您的余额为：",Fmoney)
                    break
                else:
                    if Ran3==3:
                        print("庄家胜")
                        Fmoney -= ante
                        print("您的余额为：",Fmoney)

                        break
                    else:
                        if Ran3==12:
                            print("庄家胜")
                            Fmoney -= ante
                            print("您的余额为：",Fmoney)

                            break
                        else:
                            Ran1 = random.randint(1, 6)
                            print("玩家摇出了",Ran1,"点")
                            Ran2 = random.randint(1, 6)
                            print("玩家摇出了", Ran2, "点")
                            Ran4=Ran1+Ran2
                            if Ran4==7:
                                print("庄家胜")
                                Fmoney -= ante
                                print("您的余额为：",Fmoney)

                                break
                            else:
                                if Ran4==Ran3:
                                    print("玩家胜")
                                    Fmoney += ante
                                    print("您的余额为：",Fmoney)

                                    break
    if Fmoney<=0:
        judge=input("您的余额不足是否继续充值，输入是充值，输入其他退出：")
        if judge == "是":
            cz = int(input("输入金额："))
            if cz > 0:
                Fmoney += cz
                print("您的余额为：",Fmoney)
                continue
        else:
            break
    tu=input("继续游戏输入F，输入其他均退出：")
    if tu!="F":
        break