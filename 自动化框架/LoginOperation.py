import time
class LoginOperation:

    def __init__(self,driver):# 全局用的都是一个driver
        self.driver = driver

    def login(self,username,pwd):
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(pwd)
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='submit']").click()
        time.sleep(3)
    def getSuccessResult(self):
        return self.driver.title













