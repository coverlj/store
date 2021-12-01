import random
a=random.randint(0,2)
money=0
if a == 0:
    dress="昌平"
    legmoney=3
    shop = "沙县小吃"
    clientdress="103室"
    food="鸡腿饭"
if a == 1:
    dress="沙河"
    legmoney = 2
    shop = "黄焖小屋"
    clientdress = "206室"
    food="黄焖猪蹄"
if a == 2:
    dress="回龙观"
    legmoney = 4
    shop = "KFC"
    clientdress = "303室"
    food="儿童套餐"
dict_shop = {dress: {shop: food, "跑腿费": legmoney, "客户地址": clientdress}}
dict_client = {"昌平": {"翻斗花园": "103室"},
                   "沙河": {"红楼": "206室"},
                   "回龙观": {"幸福小区": "303室"}
                   }
w=0
print(dict_shop,w)
def swm(dress1,money):
    w=0
    while True:
        if w == 0:
            for y in dict_shop:
                if dress1 == y:
                    a2 = input("先有一个订单等待接单，是否查看订单信息？输入是查看，输入其他退出系统！！")
                    if a2 == "是":
                        print("店铺位置在：", dress, "店铺名称为：", shop)
                        a3 = input("您是否确定接单？输入是接单，输入其他退出系统！！")
                        if a3 == "是":
                            print("客户地址在：", clientdress)
                            print("派送员正在路上，请您耐心等待！")
                            dict_client[dress1].update({shop: food})
                            money += legmoney
                            print("正在进行订单为：", dict_client[y])
                            print("您的外卖已送达，支付", legmoney, "元")
                            while True:
                                fmoney = int(input("请输入付款金额："))
                                if fmoney == legmoney:
                                    print("感谢您的使用！！")
                                    print("对方已支付", legmoney, "您的跑腿费：", money)
                                    w = 1
                                    break
                                elif fmoney > legmoney:
                                    tk = fmoney - legmoney
                                    print("您付的金额超出", tk, "元", "我们将通过支付宝或微信退款给您")
                                    xz = input("请您选择支付宝或微信退款（输入微信或支付宝）：")
                                    if xz == "支付宝":
                                        print("请查看您的支付宝余额账单，退款将于24小时退还给您")
                                        w = 1
                                        break
                                    elif xz == "微信":
                                        print("请查看您的微信余额账单，退款将于24小时退还给您")
                                        w = 1
                                        break
                                elif fmoney < legmoney:
                                    bc = legmoney - fmoney
                                    print("您还缺", bc, "元", "您选择支付宝或微信退款支付")
                                    xz = input("请您选择支付宝或微信付款（输入微信或支付宝）：")
                                    if xz == "支付宝":
                                        print("支付宝余额已扣款", bc, "元")
                                        w = 1
                                        break
                                    elif xz == "微信":
                                        print("微信余额已扣款", bc, "元")
                                        w = 1
                                        break
                            print("完成订单为：", dict_client[y])

                else:
                    print("您输入的地址有误，请重新输入")
        else:
            break
for i in dict_shop:
    info='''
         ============派送区域编号===============
                   
                编号：              地址
                01                 昌平
                02                 沙河
                03                回龙观
            
            '''
    print(info)
    a = input("请输入您的派送区域：")
    if a=="01":
        dress1="昌平"
        swm(dress1,0)
        break
    if a=="02":
        dress1 = "沙河"
        swm(dress1,0)
        break
    if a=="03":
        dress1 = "回龙观"
        swm(dress1,0)
        break
