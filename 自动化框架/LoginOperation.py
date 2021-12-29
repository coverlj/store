import time
from selenium.webdriver.common.by import By
class LoginOperation:
    def __init__(self,driver):
        self.driver = driver
    def login(self,username,pwd):
        self.driver.find_element(By.XPATH,"//*[@id='loginname']").send_keys(username)
        self.driver.find_element(By.XPATH,"//*[@id='password']").send_keys(pwd)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[@id='submit']").click()
        time.sleep(3)
    def getSuccessResult(self):
        return self.driver.title













