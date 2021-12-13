
from bank import bank
bank_choice = {"1":"开户","2":"存钱","3":"取钱","4":"转账","5":"查询","6":"切换","7":"Bye"}
class weco:
    __myinfo = '''
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
    __welcome ='''
***********************************
*      中国%s账户管理系统       *
***********************************
*               选项              *
    '''

    __welcome_item ='''
*               {0}.{1}            *
        '''

    def getmyinfo(self):
        return self.__myinfo
    def getwelcome(self):
        return self.__welcome
    def getwelcome_item(self):
        return self.__welcome_item
    def getprint_welcome(self):
        bk = bank()
        print(self.__welcome % (bk.getBank_name()), end="")
        keys = bank_choice.keys()
        for i in keys:
            print(self.__welcome_item.format(i, bank_choice[i]))
        print("**********************************")
    def getisExists(self,chose, data):
        if chose in data:
            return True
        return False