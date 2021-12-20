from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from 工商银行完整版 import bank_addUser
from csj import dq
xl=dq()
dabank =xl.xlrd_excel("d:/工商银行数据测试报告.xls",8)
@ddt
class TestBank(TestCase):
    @data(*dabank)
    @unpack  # 解包
    def testAdduser(self, a, b, c,d,e,f,g,h):
        wt = dq()
        s=bank_addUser(a, b, c,d,e,f,g)
        if s == h:
            wt.xlwt_excel(a,"成功",8,"d:/工商银行数据测试报告.xls")
        else:
            wt.xlwt_excel(a,"失败",8,"d:/工商银行数据测试报告.xls")
        self.assertEqual(s,h)