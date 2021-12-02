# from random import randint
import random
print("*********************")
print("*     中国工商银行     *")
print("*     账户管理系统     *")
print("*        V1.0       *")
print("*********************")
print("*1、开户              *")
print("*2、存钱              *")
print("*3、取钱              *")
print("*4、转账              *")
print("*5、查询              *")
print("*6.Bye!              *")
print("*********************")
#定义一个空字典,当作数据库
bank={}
#bank={'Frank': {'account': 29073386, 'password': '123456', 'country': '中国', 'province': '山东', 'street': '1大街', 'door': '001', 'bank_name': '中国工商银行', 'money': 0}
bank_name="中国工商银行"
#定义方法————用来添加用户的
def useradd():
    account=random.randint(10000000,99999999)
    username=input("请输入您的姓名")
    password=input("请输入您的密码")#如果定义为str   ”“
    country=input("\t\t请输入您的国家")#\t表示一个tab
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入你的街道")
    door=input("\t\t请输入您的门牌号")
    gift=bankadd(account,username,password,country,province,street,door)#位置对应
    if gift =="1" :
        print("开户成功,一下是您的详细信息")
        #模板
        info='''
                --------工商银行-------
                    1、账号：%s
                    2、姓名：%s
                    3、密码：******
                    4、国家：%s
                    5、省份：%s
                    6、街道：%s
                    7、门牌：%s
                    8、余额：%s
        '''
        print(info % (account,username,country,province,street,door,bank[username]["money"]))
    elif gift =="2":
        print("请使用其他用户")
    elif gift =="3":
        print("数据库已满")

#往字典里面存数据
def bankadd(account,username,password,country,province,street,door):
    if username in bank:#  姓名在不在bank的键里
        return "2"
    elif len(bank)>=100:
        return "3"
    bank[username]={
        "account":account,#从useradd的account获取的随机数
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "bank_name":bank_name,
        "money":0
    }
    return "1"
#存钱
def depositadd(username,b):
        if username in bank.keys():
            bank[username]["money"]+=b
            return True
        else:
            return False

def takeadd(username,userpass,b):
    if username in bank.keys():
        if userpass == bank[username]["password"]:
            bank[username]["money"] -= b
            return True
        else:
            return False
    else:
        return False

def transfer_accountsadd(outname,inname,outuserpasswore,outmoney):
    if outname in bank.keys() and inname  in bank.keys():
        if outuserpasswore == bank[outname]["password"]:
            if outmoney<bank[outname]["money"]:
                bank[outname]["money"] -= outmoney
                bank[inname]["money"] += outmoney
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1


def queryadd(username,userpasssword):
    if username in bank.keys():
        if userpasssword==bank[username]["password"]:
            return 0
        else:
            return 1
    else:
        return 2




def deposit():
    username=input("请输入您的姓名：")
    moneydep=int(input("请输入存钱的金额"))
    jg=depositadd(username,moneydep)
    if jg==True:
        info = '''
        ====存款成功以下为本次存款信息====
                用户名：%s
                余额：%s
                开户行：%s
        '''
        print(info % (username, bank[username]["money"], bank_name))
    else:
        print("账号不存在")

def takemoney():
    username=input("请输入您的姓名：")
    userpassword = input("请输入您的密码：")
    moneytake=int(input("请输入存钱的金额"))
    jg=takeadd(username,userpassword,moneytake)
    if jg==True:
        info = '''
        ====取款成功以下为本次存款信息====
                用户名：%s
                余额：%s
                开户行：%s
        '''
        print(info % (username, bank[username]["money"], bank_name))
    else:
        print("账号不存在")


def transfer_accounts():
    outname=input("请输入转出的账户：")
    inname = input("请输入转入的账户：")
    outuserpasswore=input("请输入转出账户的密码：")
    outmoney=int(input("请输入转出金额："))
    mb=transfer_accountsadd(outname,inname,outuserpasswore,outmoney)

    if mb==0:
        print("正常")
        info = '''
                ====转账成功以下为本次存款信息====
                        付款用户名：%s
                        收款用户名：%s
                        转账金额：%s
                        转出账户余额：%s
                        转入账户余额：%s
                        开户行：%s
                '''
        print(info % (outname,inname ,outmoney,bank[outname]["money"], bank[inname]["money"],bank_name))
    elif mb==1:
        print("账号不对")
    elif mb==2:
        print("密码不对")
    elif mb==3:
        print("钱不够")



def query():
    username=input("请输入用户名：")
    userpasssword=input("请输入账号密码：")
    mb=queryadd(username,userpasssword)
    if mb==0:
        info = '''
                ====查询成功以下为本次查询信息====
                        当前账号：%s
                        密码：%s
                        余额：%s
                        用户居住地址：国家：%s 省份：%s 街道：%s 门牌号：%s
                        当前账户的开户行：%s
                '''
        print(info % (bank[username]["account"],userpasssword,bank[username]["money"],bank[username]["country"],
            bank[username]["province"],bank[username]["street"],bank[username]["door"],bank_name))
    elif mb==1:
        print("账号不对")
    elif mb==2:
        print("密码不对")
    elif mb==3:
        print("钱不够")
while True:
    box=input("请输入编号")
    if box=="1":
        print("1、开户")
        useradd()
    elif box =="2":
        print("2、存钱")
        deposit()
    elif box == "3":
        print("3、取钱")
        takemoney()

    elif box == "4":
        print("4、转账")
        transfer_accounts()
    elif box == "5":
        print("5、查询")
        query()
    elif box == "6":
        print("是否退出“中国工商银行账户管理系统？")
        pd=input("输入是退出系统，输入其他继续使用：")
        if pd=="是":
            print("感谢您的使用，祝您健康愉悦！！")
            break
        else:
            continue
