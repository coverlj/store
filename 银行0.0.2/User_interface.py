from welcome import weco
from bank import bank
from Input import Input

wc = weco()
IP=Input()
my=bank()
my.chooseBank_name(input("请输入您选择的银行:"))
while True:
    wc.getprint_welcome()
    chose = IP.getinputHelp("选项")
    if wc.getisExists(chose,my.getbankchoice()):
        if chose == "1":
            my.adduser()
        elif chose == "2":
            my.saveMoney()
        elif chose == "3":
            my.takeMoney()
        elif chose == "4":
            my.transformMoney()
        elif chose == "5":
            my.selectUser()
        elif chose == "6":
            my.chooseBank_name(input("请输入您选择的银行:"))
        elif chose == "7":
            print("Bye")
            break
    else:
        print("不存在该选项，别瞎弄！")
