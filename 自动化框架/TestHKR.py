from selenium import webdriver
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from LoginOperation import LoginOperation
import time
from dx import dxwj
d=dxwj()
@ddt
class Testlogin(TestCase):
     @data(*d.xlrd_excel("d:/HKR.xls",3))
     @unpack
     def testuserLogin(self,a,b,c):
         username=a
         pwd=b
         expect=c
         driver = webdriver.Chrome()
         driver.get("http://localhost:8081/HKR")
         driver.maximize_window()
         loginOpera = LoginOperation(driver)
         loginOpera.login(username,pwd)
         result = loginOpera.getSuccessResult()
         time.sleep(1)
         if result != expect:
             # driver.save_screenshot(username + "----" + pwd + ".jpg")
             d.xlwt_excel(username, result, 3, "d:/HKR.xls")
             d.xlwt_excel(username, "不通过", 4, "d:/HKR.xls")
         else:
             # driver.save_screenshot(username + "----" + pwd + ".jpg")
             d.xlwt_excel(username,result, 3, "d:/HKR.xls")
             d.xlwt_excel(username, "通过", 4, "d:/HKR.xls")
         driver.quit()
         self.assertEqual(result,expect)






















