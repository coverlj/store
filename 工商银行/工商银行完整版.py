# author:jason
import random
from DBUtils import  update
from DBUtils import select
#银行库
bank = {}
bank_name = "中国工商银行昌平支行"
bank_choice = {"1":"开户","2":"存钱","3":"取钱","4":"转账","5":"查询","6":"Bye"}  # 银行业务选项
# 开户成功的信息模板
myinfo='''
    \033[0;32;40m
    ------------账户信息------------
    账号：{account}
    姓名：{username}
    密码：{password}
    地址：
        国家：{country}
        省份：{province}
        街道：{street}
        门牌号：{door}
    账户余额：{money}
    注册银行名：{bank_name}
    -------------------------------
    \033[0m
'''


# 欢迎模板
welcome = '''
***********************************
*      中国工商银行账户管理系统       *
***********************************
*               选项              *
'''

welcome_item = '''*              {0}.{1}             *'''

def print_welcome():
    print(welcome,end="")
    keys = bank_choice.keys()
    for i in keys:
        print(welcome_item.format(i,bank_choice[i]))
    print("**********************************")

# 输入帮助方法：chose是打印选项
def inputHelp(chose,datatype="str"):
    while True:
        print("请输入",chose,":")
        i = input(">>>:")
        if len(i) == 0:
            print("该项不能为空！请重新输入！")
            continue
        if datatype != "str":
            return int(i)
        else:
            return i

# 判断是否存在该银行选项
def  isExists(chose,data):
    if chose in data:
        return True
    return False


# 获取随机码
def  getRandom():
    li = "0123456789qwertyuiopasdfghjklzxcvbnmZXCVBNMASDFGHJKLQWERTYUIOP"
    string = ""
    for i in range(8):
        string =  string + li[int(random.random()* len(li))]
    return string

# 通过账号获取账户信息
def findByAccount(account):
    for i in bank.keys():
        if bank[i]["account"] == account:
            return i
    return None

# 银行的开户方法
def bank_addUser(username,password,country,province,street,door,money):
    # 查询是否已满
    sql = "select count(*) from usermessage" # (5)
    param = []
    data = select(sql,param)
    if len(data) >= 100:
        return 3


    # 查询是否存在
    sql1 = "select * from usermessage where username = %s"
    param1 = [username]
    data1 = select(sql1,param1)
    if len(data1) > 0:
        return 2

    # 插入数据
    else:
        sql2 = " insert into usermessage values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param2 = [getRandom(),username,password,country,province,street,door,money,'2021-12-07',bank_name]
        update(sql2,param2)
    return 1

# 银行的存钱方法
def bank_saveMoney(ac,money):
    sql2 ="select * from usermessage where sccount = %s"
    param2=[ac]
    data2=select(sql2,param2)
    if len(data2) > 0:
        sql3="update usermessage set money = money + %s where sccount = %s  "
        param3=[money,ac]
        update(sql3,param3)
        return True
    else:
        return False

# 银行的查询功能
def bank_selectUser(account,password):
    sql4="select * from usermessage where sccount = %s "
    param4=[account]
    data4=select(sql4,param4)
    if len(data4)>0:
      sql5="select * from usermessage where pword = %s "
      param5=[password]
      data5=select(sql5,param5)
      if len(data5)>0:
        for i in data4:
            print(i)
      else:
        print("用户密码错误！")
    else:
        print("该用户不存在！")

# 银行的取钱功能
def bank_takeMoney(account,password,money):
    sql6="select * from usermessage where sccount = %s"
    param6=[account]
    data6=select(sql6,param6)
    if len(data6)>0:
        sql7 = "select * from usermessage where pword = %s and sccount = %s "
        param7 = [password,account]
        data7 = select(sql7, param7)
        if len(data7) > 0:
            sql8="select * from usermessage where money > %s and sccount = %s"
            param8=[money,account]
            data8=select(sql8,param8)
            if len(data8)>0:
                sql9="update usermessage  set money = money - %s  where sccount = %s"
                param9=[money,account]
                update(sql9,param9)
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1

# 银行的转账功能
def bank_transformMoney(outputaccount,inputaccount,outputpassword,outputmoney):
    sql10="select * from usermessage where sccount = %s "
    param10=[outputaccount]
    data10=select(sql10,param10)
    if len(data10)>0:
        sql11 = "select * from usermessage where sccount = %s "
        param11 = [inputaccount]
        data11 = select(sql11, param11)
        if len(data11) > 0:
            sql12="select * from usermessage where pword = %s and sccount = %s "
            param12=[outputpassword,outputaccount]
            data12=select(sql12,param12)
            if len(data12) > 0:
                sql13 = "select * from usermessage where money > %s and sccount = %s"
                param13 = [outputmoney, outputaccount]
                data13 = select(sql13, param13)
                if len(data13) > 0:
                    sql14="update usermessage set money = money - %s where sccount = %s"
                    param14=[outputmoney,outputaccount]
                    sql15="update usermessage set money = money + %s where sccount = %s"
                    param15=[outputmoney,inputaccount]
                    update(sql15,param15)
                    update(sql14,param14)
                    return 5
                else:
                    return 3
            else:
                return 2
        else:
            return 1
    else:
        return 1
# 开户方法
def  addUser():
    username = inputHelp("用户名")
    password = inputHelp("密码")
    country = inputHelp("居住地址：1.国家：")
    province =  inputHelp("省份")
    street = inputHelp("街道")
    door = inputHelp("门牌号")
    money =  inputHelp("银行卡余额","int")

    # 调用银行的开户方法完成开户操作  返回 1 2 3
    status = bank_addUser(username,password,country,province,street,door,money)
    # 判断1   2   3
    if status == 1:
        sql16="select * from usermessage where username= %s"
        param16=username
        data=select(sql16,param16)
        for i in data:
            print(i)
        print("恭喜开户成功！以上是您的开户信息：")
        # print(myinfo.format(account=bank[username]["account"],
        #                     username=username,
        #                     password=bank[username]["password"],
        #                     country=bank[username]["country"],
        #                     province=bank[username]["province"],
        #                     street=bank[username]["street"],
        #                     door=bank[username]["door"],
        #                     money=bank[username]["money"],
        #                     bank_name=bank[username]["bank_name"]
        #                     ))
    elif status == 2:
        print("改用户已经存在！请携带证件到其他银行办理！谢谢！！！！！")
    elif status == 3:
        print("银行库已满！请携带证件到其他银行办理！谢谢！！！！！")

# 存钱
def saveMoney():
    account = inputHelp("账号")
    m =  inputHelp("存入的金额","int")

    flag = bank_saveMoney(account,m)

    if flag:
        print("存储成功!您的个人信息为：")
        sql17 = "select * from usermessage where sccount= %s"
        param17 = account
        data = select(sql17, param17)
        for i in data:
            print(i)
        # uname = findByAccount(account)
        # user = bank[uname]
        # print(myinfo.format(account=user["account"],
        #                     username=uname,
        #                     password=user["password"],
        #                     country=user["country"],
        #                     province=user["province"],
        #                     street=user["street"],
        #                     door=user["door"],
        #                     money=user["money"],
        #                     bank_name=user["bank_name"]
        #                     ))
    else:
        print("对不起，您的个人信息不存在！请先开户后再次操作！")

# 取钱
def takeMoney():
    account = inputHelp("账户")
    password =  inputHelp("密码")
    tmoney = inputHelp("取出金额","int")

    f = bank_takeMoney(account,password,tmoney)

    if f == 1:
        print("该用户不存在！")
    elif f == 2:
        print("密码错误！")
    elif f == 3:
        print("取款金额不足！")
    elif f == 0:
        print("取款成功！")
        bank_selectUser(account,password)


# 转账功能
def transformMoney():
    output = inputHelp("转出的账号")
    input = inputHelp("转入的账号")
    outputpass =  inputHelp("转出的密码")
    outputmoney = inputHelp("要转出的金额","int")

    f = bank_transformMoney(output,input,outputpass,outputmoney)

    if f == 1:
        print("转出或转入的账号不存在！")
    elif f == 2:
        print("输入密码错误！")
    elif f == 3:
        print("转账金额不足！")
    else:
        print("转账成功！")
        print("您的个人信息：")
        bank_selectUser(output,outputpass)

# 查询账户方法
def selectUser():
    account = inputHelp("账号")
    password = inputHelp("密码")

    bank_selectUser(account,password)

# 核心程序
while True:

    print_welcome()
    chose = inputHelp("选项")
    if isExists(chose,bank_choice):
        if chose  == "1":
            addUser()
        elif chose == "2":
            saveMoney()
        elif chose == "3":
            takeMoney()
        elif chose == "4":
            transformMoney()
        elif chose == "5":
            selectUser()
        elif chose == "6":
            print("Bye,Bye您嘞！！！！")
            break
    else:
        print("不存在改选项，别瞎弄！")