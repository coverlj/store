'''
    Frank的商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条。
    任务：尽量多的添加商品
    任务：10个辣条优惠券（0.3），20个威猛先生优惠券（0.9），免单一张优惠券，先整体打折8后在单独打折，
        在进入商城时，随机抽取优惠券，在最后结算使用改优惠券。
'''
#超市
import random
a=random.randint(1,3)
print(a)
b=1
c=1
d=1
e=0
f=0.8
if a==1:
    e=0.3
    print("恭喜您抽到3折辣条优惠券")
if a==2:
    e=0.9
    print("恭喜您抽到9折威猛先生优惠券")
if a==3:
    e=0
    print("恭喜您抽到大奖免单")
shop=[
    # 0     1
    ["酱油",20],#0
    ["醋",15],#1
    ["腊肠",50],#2
    ["辣条",5.5],#3
    ["电饭煲",299],
    ["威猛先生",60],
    ["软华子",70],#抽烟
    ["鸡蛋面",10]
]
#购物车
mycar=[]
#初始化钱包
money=1000
omoney=money
#       枚举
while True:
    for i in enumerate(shop):#列举商品
        print(i)
    o=input("请选择商品")#str  转换成int类型
    # 一个元素在某一个容器里面：
    if o.isdigit():#.isdigit判读字符串内是不是由数字组成
        o=int(o)#把str转换成int
        if o <len(shop):#判断输入的范围
            if money>shop[o][1]:#钱够不够
                mycar.append(shop[o])#加入购物车
                if a==3 and d>0:
                    d=d-1
                    print(d)
                    money = money - shop[o][1]* f * e
                    e=1
                    print("此商品已经加入购物车，您的余额为：", money)
                    continue
                if o==3 and a>0:
                    a-=1
                    money=money-shop[o][1]*f*e#减钱
                    e=1
                    print("此商品已经加入购物车，您的余额为：",money)
                    continue
                if o==5 and b>0:
                    b-=1
                    money = money - shop[o][1]* f * e  # 减钱
                    e=1
                    print("此商品已经加入购物车，您的余额为：", money)
                    continue
                else:
                    money=money-shop[o][1]*f
                    print("此商品已经加入购物车，您的余额为：", money)
                    continue
            else:print("穷鬼，gun")
        else:print("请输入正确的商品编号")
    elif o =="q" or o=="Q":#输入内容退出并打印小条
        omoney-=money
        print("再见,以下是您购买的商品")
        for i in enumerate(mycar):
            print(i)
        print("已用金额为：",omoney)
        break
    else:print("您输入的有误")