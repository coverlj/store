from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from Calc import  Calc
from csj import dq
xl=dq()
dacalc =xl.xlrd_excel("d:/计算器数据测试报告.xls",3)   # 参数化数据用文件参数化
@ddt
class TestCalc1(TestCase):
    @data(*dacalc)
    @unpack # 解包
    def testAdd(self,a,b,c):
        calc = Calc()
        wt = dq()
        s = calc.add(a,b)
        if s == c:
            wt.xlwt_excel(a,"成功",3,"d:/计算器数据测试报告.xls")
        else:
            wt.xlwt_excel(a,"失败",3,"d:/计算器数据测试报告.xls")
        self.assertEqual(s,c)