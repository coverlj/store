from threading import Thread
import time
import threading
import sys
egg_tart_basket=0
start=time.time()
global purchase_quantity
class cooker(Thread):
    m1 = threading.Lock()
    name=""
    salary=0
    egg_tart_quantity=0
    def run(self) -> None:
        global egg_tart_basket
        while True:
            end = time.time()
            self.m1.acquire()
            if egg_tart_basket == 500:
                print("篮子里已经装满500个蛋挞了，可以开始抢购了")
                time.sleep(3)
            elif egg_tart_basket<500:
                self.egg_tart_quantity += 1
                egg_tart_basket += 1
                print(self.name,"厨子做了",self.egg_tart_quantity,"个蛋挞")
                print(" ", end="")
            if end - start >= 20:
                print("本店只营业3分钟！不卖了！！！！")
                sys.exit(0)
            self.m1.release()
class shopper(Thread):
    m2 = threading.Lock()
    name=""
    remaining_sum=30000
    purchase_quantity=0
    def run(self) -> None:
        global egg_tart_basket
        while True:
            end = time.time()
            if end - start >= 20:
                sys.exit(0)
            self.m2.acquire()
            if egg_tart_basket<1:
                print("篮子里没有蛋挞了")
                time.sleep(2)
            elif egg_tart_basket>1:
                self.purchase_quantity += 1
                egg_tart_basket -= 1
                self.remaining_sum -= 3
                print(self.name,"您的余额为：",self.remaining_sum)
                time.sleep(0.1)
            elif self.remaining_sum<3:
                print("您的余额不足")
                break
            self.m2.release()

c1 = cooker()
c1.name="厨子1号"
c2 = cooker()
c2.name="厨子2号"
c3 = cooker()
c3.name="厨子3号"
s1 = shopper()
s1.name="路人1号"
s2 = shopper()
s2.name="路人2号"
s3 = shopper()
s3.name="路人3号"
s4 = shopper()
s4.name="路人4号"
s5 = shopper()
s5.name="路人5号"
s6 = shopper()
s6.name="路人6号"
c1.start()
c2.start()
c3.start()
s1.start()
s2.start()
s3.start()
s4.start()
s5.start()
s6.start()

















