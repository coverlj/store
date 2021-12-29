from selenium import webdriver
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
import time
from dx import dxwj
from UserModule import Head_Sculpture_Operation
d=dxwj()
@ddt
class TestScwj(TestCase):
    @data(*d.xlrd_excel("d:/HKRsctx.xls",3))
    @unpack
    def testscwj(self,a,b,c):
        username=a
        pwd=b
        expect=c
        driver = webdriver.Chrome()
        driver.get("http://localhost:8081/HKR")
        driver.maximize_window()
        Head_Sculpture_Operations = Head_Sculpture_Operation(driver)
        result = Head_Sculpture_Operations.sctx(username, pwd)
        time.sleep(1)
        if result != expect:
            # driver.save_screenshot(username + "----" + pwd + ".jpg")
            d.xlwt_excel(username, result, 3, "d:/HKRsctx.xls")
            d.xlwt_excel(username, "不通过", 4, "d:/HKRsctx.xls")
        else:
            # driver.save_screenshot(username + "----" + pwd + ".jpg")
            d.xlwt_excel(username, result, 3, "d:/HKRsctx.xls")
            d.xlwt_excel(username, "通过", 4, "d:/HKRsctx.xls")
        driver.quit()
        self.assertEqual(result,expect)