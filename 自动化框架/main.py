from HTMLTestRunner import  HTMLTestRunner
import  unittest
import os
class bg:
    def scbg(self,cswj,titlename,descriptionname,filename):
        tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern=cswj)
        runner = HTMLTestRunner.HTMLTestRunner(
            title = titlename,
            description=descriptionname,
            verbosity=1,
            stream = open(file=filename,mode="w+",encoding="utf-8")
        )

        runner.run(tests)

b=bg()
b.scbg("TestHKR.py","HKR登陆测试","登陆测试【成功、失败】","HKRLogin.html")
b.scbg("TestXg.py","HKR修改头像测试","修改测试【成功、失败】","HKRxgtx.html")
b.scbg("TestSC.py","HKR上传头像测试","上传测试【成功、失败】","HKRscwj.html")
b.scbg("TestTc.py","HKR退出系统测试","退出测试【成功、失败】","HKRtcxt.html")






