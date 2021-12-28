from HTMLTestRunner import  HTMLTestRunner
import  unittest
import os
tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")
runner = HTMLTestRunner.HTMLTestRunner(
    title = "HKR登陆测试",
    description="登陆测试【成功、失败】",
    verbosity=1,
    stream = open(file="HKR.html",mode="w+",encoding="utf-8")
)

runner.run(tests)













