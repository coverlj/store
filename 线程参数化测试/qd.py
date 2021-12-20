from threading import Thread
import threading
from HTMLTestRunner import HTMLTestRunner
import unittest
import os
class testxc(Thread):
    __pattern=""
    __titlename=""
    __descriptionname=""
    __filename=""
    m1 = threading.Lock()
    def setpattern(self,name):
        self.__pattern=name
    def getpattern(self):
        return self.__pattern
    def settitlename(self,name):
        self.__titlename=name
    def gettitlename(self):
        return self.__titlename
    def setdescriptionname(self,name):
        self.__descriptionname=name
    def getdescriptionname(self):
        return self.__descriptionname
    def setfilename(self,name):
        self.__filename=name
    def getfilename(self):
        return self.__filename
    def run(self) -> None:
        self.m1.acquire()
        tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern=self.__pattern)
        runner = HTMLTestRunner.HTMLTestRunner(
            title=self.__titlename,
            description=self.__descriptionname,
            verbosity=1,
            stream=open(file=self.__filename, mode="w+", encoding="utf-8")
        )
        runner.run(tests)
        self.m1.release()
t1=testxc()
t2=testxc()
t1.setpattern("TestCalc.py")
t1.settitlename("计算器的测试报告")
t1.setdescriptionname("计算器加法测试报告")
t1.setfilename("calc_Parameterization_test1.html")
t2.setpattern("TestBank.py")
t2.settitlename("银行的测试报告")
t2.setdescriptionname("银行开户测试报告")
t2.setfilename("bank_Parameterization_test1.html")
t1.start()
t2.start()