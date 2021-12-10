from Utils import lianjie
from Service_Charge import sercha
import random
bank_choice = {"1":"开户","2":"存钱","3":"取钱","4":"转账","5":"查询","6":"切换","7":"Bye"}
myinfo='''
            ------------账户信息------------
            账号：%s
            姓名：%s
            密码：%s
            地址：
                国家：%s
                省份：%s
                街道：%s
                门牌号：%s
            账户余额：%s
            注册银行名：%s
            -------------------------------
        '''


# 欢迎模板
welcome = '''
***********************************
*      中国%s账户管理系统       *
***********************************
*               选项              *
'''

welcome_item = '''*              {0}.{1}             *'''










class bank:
    __bank_name=""
    __bank_dress=""
    __bnak_database=""
    __bank_choice = {"1":"开户","2":"存钱","3":"取钱","4":"转账","5":"查询","6":"Bye"}

    def print_welcome(self):
        print(welcome % (self.__bank_name), end="")
        keys = bank_choice.keys()
        for i in keys:
            print(welcome_item.format(i, bank_choice[i]))
        print("**********************************")

    def isExists(self,chose, data):
        if chose in data:
            return True
        return False

    def setBank_name(self,bankname):
        if bankname=="工商银行" or bankname=="农业银行":
            self.__bank_name=bankname
        else:
            print("未开通",bankname,"很抱歉给您带来困扰！！")
    def setBank_dress(self):
        if self.__bank_name=="工商银行":
            self.__bank_dress="中国工商银行昌平支行"
        elif self.__bank_name=="农业银行":
            self.__bank_dress="中国农业银行昌平支行"
    def setbankdata(self,database):
        self.__bnak_database=database
    def chooseBank_name(self,name):
        if name=="工商银行":
            self.setBank_name("工商银行")
            self.setbankdata("icbc")
            gs=lianjie()
            gs.setDatabase("icbc")
        elif name=="农业银行":
            self.setBank_name("农业银行")
            self.setbankdata("abc")
            ny=lianjie()
            ny.setDatabase("abc")
        else:
            print("暂时未开通该银行的业务系统，很抱歉给您带来困扰！！")

    def inputHelp(self,chose,datatype="str"):
        while True:
            print("请输入", chose, ":")
            i = input(">>>:")
            if len(i) == 0:
                print("该项不能为空！请重新输入！")
                continue
            if datatype != "str":
                return int(i)
            else:
                return i

    def getRandom(self):
        li = "0123456789qwertyuiopasdfghjklzxcvbnmZXCVBNMASDFGHJKLQWERTYUIOP"
        string = ""
        for i in range(8):
            string = string + li[int(random.random() * len(li))]
        return string

    # 通过账号获取账户信息

    def bank_addUser(self,username, password, country, province, street, door, money):
        # 查询是否已满
        lj=lianjie()
        lj.setDatabase(self.__bnak_database)
        sql = "select count(*) from usermessage"  # (5)
        param = []
        data = lj.select(sql, param)
        if len(data) >= 100:
            return 3

        # 查询是否存在
        sql1 = "select * from usermessage where username = %s"
        param1 = [username]
        data1 = lj.select(sql1, param1)
        if len(data1) > 0:
            return 2

        # 插入数据
        else:
            sql2 = " insert into usermessage values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            param2 = [self.getRandom(), username, password, country, province, street, door, money, '2021-12-07', self.__bank_name]
            lj.update(sql2, param2)
        return 1

    def adduser(self):
        username = self.inputHelp("请输入用户名")
        password = self.inputHelp("密码")
        country = self.inputHelp("居住地址：1.国家：")
        province = self.inputHelp("省份")
        street = self.inputHelp("街道")
        door = self.inputHelp("门牌号")
        money = self.inputHelp("银行卡余额", "int")

        # 调用银行的开户方法完成开户操作  返回 1 2 3
        status = self.bank_addUser(username, password, country, province, street, door, money)
        # 判断1   2   3
        if status == 1:
            lj=lianjie()
            lj.setDatabase(self.__bnak_database)
            sql16 = "select * from usermessage where username= %s"
            param16 = username
            data16 = list(lj.select(sql16, param16))
            print("恭喜开户成功！以下是您的开户信息：")
            print(myinfo % (
            data16[0][0], data16[0][1], data16[0][2], data16[0][3], data16[0][4], data16[0][5], data16[0][6],
            data16[0][7], data16[0][9]))
        elif status == 2:
            print("改用户已经存在！请携带证件到其他银行办理！谢谢！！！！！")
        elif status == 3:
            print("银行库已满！请携带证件到其他银行办理！谢谢！！！！！")

    def bank_saveMoney(self,ac, money):
        lj=lianjie()
        lj.setDatabase(self.__bnak_database)
        sql2 = "select * from usermessage where account = %s"
        param2 = [ac]
        data2 = lj.select(sql2, param2)
        if len(data2) > 0:
            sql3 = "update usermessage set money = money + %s where account = %s  "
            param3 = [money, ac]
            lj.update(sql3, param3)
            return True
        else:
            return False

    def saveMoney(self):
        account = self.inputHelp("账号")
        m = self.inputHelp("存入的金额", "int")
        flag = self.bank_saveMoney(account, m)
        if flag:
            lj=lianjie()
            lj.setDatabase(self.__bnak_database)
            print("存储成功!您的个人信息为：")
            sql17 = "select * from usermessage where account= %s"
            param17 = account
            data17 = list(lj.select(sql17, param17))

            print(myinfo % (
            data17[0][0], data17[0][1], data17[0][2], data17[0][3], data17[0][4], data17[0][5], data17[0][6],
            data17[0][7], data17[0][9]))
        else:
            print("对不起，您的个人信息不存在！请先开户后再次操作！")

    def bank_takeMoney(self,account, password, money):
        lj=lianjie()
        lj.setDatabase(self.__bnak_database)
        sql6 = "select * from usermessage where account = %s"
        param6 = [account]
        data6 = lj.select(sql6, param6)
        if len(data6) > 0:
            sql7 = "select * from usermessage where pword = %s and account = %s "
            param7 = [password, account]
            data7 = lj.select(sql7, param7)
            if len(data7) > 0:
                sql8 = "select * from usermessage where money > %s and account = %s"
                param8 = [money, account]
                data8 = lj.select(sql8, param8)
                if len(data8) > 0:
                    sql9 = "update usermessage  set money = money - %s  where account = %s"
                    param9 = [money, account]
                    lj.update(sql9, param9)
                    return 0
                else:
                    return 3
            else:
                return 2
        else:
            return 1



    def takeMoney(self):
        account = self.inputHelp("账户")
        password = self.inputHelp("密码")
        tmoney = self.inputHelp("取出金额", "int")

        f = self.bank_takeMoney(account, password, tmoney)

        if f == 1:
            print("该用户不存在！")
        elif f == 2:
            print("密码错误！")
        elif f == 3:
            print("取款金额不足！")
        elif f == 0:
            print("取款成功！")
            self.bank_selectUser(account,self.__bank_name,password)




    def bank_selectUser(self,account,bankname, password):
        self.chooseBank_name(bankname)
        lj=lianjie()
        lj.setDatabase(self.__bnak_database)
        sql4 = "select * from usermessage where account = %s "
        param4 = [account]
        data4 = lj.select(sql4, param4)
        if len(data4) > 0:
            sql5 = "select * from usermessage where pword = %s and account=%s "
            param5 = [password, account]
            data5 = list(lj.select(sql5, param5))
            if len(data5) > 0:
                # for i in data4:
                #     print(i)
                print(myinfo % (
                data5[0][0], data5[0][1], data5[0][2], data5[0][3], data5[0][4], data5[0][5], data5[0][6], data5[0][7],
                data5[0][9]))
            else:
                print("用户密码错误！")
        else:
            print("该用户不存在！")

    def selectUser(self):
        account = self.inputHelp("账号")
        password = self.inputHelp("密码")
        self.bank_selectUser(account,self.__bank_name,password)

    def Peer_transfer(self,outputaccount, inputaccount, outputpassword, outputmoney):
        lj=lianjie()
        lj.setDatabase(self.__bnak_database)
        sql10 = "select * from usermessage where account = %s "
        param10 = [outputaccount]
        data10 = lj.select(sql10, param10)
        if len(data10) > 0:
            param11 = [inputaccount]
            data11 = lj.select(sql10, param11)
            if len(data11) > 0:
                sql12 = "select * from usermessage where pword = %s and account = %s "
                param12 = [outputpassword, outputaccount]
                data12 = lj.select(sql12, param12)
                if len(data12) > 0:
                    sql13 = "select * from usermessage where money > %s and account = %s"
                    param13 = [outputmoney, outputaccount]
                    data13 = lj.select(sql13, param13)
                    if len(data13) > 0:
                        sql14 = "update usermessage set money = money - %s where account = %s"
                        param14 = [outputmoney, outputaccount]
                        sql15 = "update usermessage set money = money + %s where account = %s"
                        param15 = [outputmoney, inputaccount]
                        lj.update(sql15, param15)
                        lj.update(sql14, param14)
                        return 5
                    else:
                        return 3
                else:
                    return 2
            else:
                return 1
        else:
            return 1

    def thzz(self,outputbank,output,outputpass,outputmoney,inputbank,input,inputpass):
        self.chooseBank_name(outputbank)
        lj=lianjie()
        lj.setDatabase(self.__bnak_database)
        sql10 = "select * from usermessage where account = %s "
        param10 = [output]
        data10 = lj.select(sql10, param10)
        if len(data10)>0:
            sql001 = "select * from usermessage where pword = %s "
            param001 = [outputpass]
            data001 = lj.select(sql001, param001)
            if len(data001)>0:
                sql002="select * from usermessage where money > %s"
                param002=[outputmoney]
                data002=lj.select(sql002,param002)
                if len(data002)>0:
                    self.chooseBank_name(inputbank)
                    lj = lianjie()
                    lj.setDatabase(self.__bnak_database)
                    print(lj.getDatabase())
                    sql003 = "select * from usermessage where account = %s "
                    param003 = [input]
                    data10 = lj.select(sql003, param003)
                    if len(data10) > 0:
                        sql004 = "select * from usermessage where pword = %s "
                        param004 = [inputpass]
                        data004 = lj.select(sql004, param004)
                        if len(data004)>0:
                            sxf=sercha()
                            sxf.setserchamoney(outputmoney)
                            sql005="update usermessage set money = money + %s where account = %s"
                            param005=[outputmoney,input]
                            lj.update(sql005,param005)
                            self.chooseBank_name(outputbank)
                            lj = lianjie()
                            lj.setDatabase(self.__bnak_database)
                            sql006="update usermessage set money = money - %s - %s where account = %s"
                            param006=[outputmoney,sxf.getserchamoney(),output]
                            lj.update(sql006,param006)
                            return 5
                        else:
                            return 2
                    else:
                        return 1
                else:
                    return 3
            else:
                return 2
        else:
            return 1

    def transformMoney(self):
        a=self.inputHelp("请输入编号选择同行转账编号：（1），还是异行转账编号（2）：")
        if a=="1":
            bankname=self.inputHelp("请选择您的银行名称：")
            output = self.inputHelp("转出的账号")
            input = self.inputHelp("转入的账号")
            outputpass = self.inputHelp("转出账户的密码")
            inputpass = self.inputHelp("转入账户的密码")
            outputmoney = self.inputHelp("要转出的金额", "int")

            f = self.Peer_transfer(output, input, outputpass, outputmoney)

            if f == 1:
                print("转出或转入的账号不存在！")
            elif f == 2:
                print("输入密码错误！")
            elif f == 3:
                print("转账金额不足！")
            else:
                print("转账成功！")
                print("您的个人信息：")
                self.bank_selectUser(output,bankname,outputpass)
                self.bank_selectUser(input, bankname,inputpass)
        elif a=="2":
            outputbank=self.inputHelp("输入转出账户的银行名称（XX银行）：")
            output = self.inputHelp("转出的账号")
            outputpass = self.inputHelp("转出账户的密码")
            outputmoney = self.inputHelp("要转出的金额", "int")
            inputbank=self.inputHelp("请输入转入账户的银行名称（XX银行）：")
            input = self.inputHelp("转入的账号")
            inputpass = self.inputHelp("转入账户的密码")
            d=self.thzz(outputbank,output,outputpass,outputmoney,inputbank,input,inputpass)
            if d == 1:
                print("转出或转入的账号不存在！")
            elif d == 2:
                print("输入密码错误！")
            elif d == 3:
                print("转账金额不足！")
            else:
                print("转账成功！")
                print("您的个人信息：")
                self.bank_selectUser(output,outputbank, outputpass)
                self.bank_selectUser(input,inputbank,  inputpass)
    # def make_interbank_transfers(self):
my=bank()
my.chooseBank_name(input("请输入您选择的银行:"))

while True:
    my.print_welcome()
    chose = my.inputHelp("选项")
    if my.isExists(chose,bank_choice):
        if chose  == "1":
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
        elif chose=="7":
            print("Bye")
            break
    else:
        print("不存在改选项，别瞎弄！")

