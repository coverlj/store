from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
import pywinauto
from pywinauto.keyboard import send_keys
class Head_Sculpture_Operation:
    def __init__(self,driver):
        self.driver = driver
    def xgtx(self,username,pwd):
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(pwd)
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='submit']").click()
        time.sleep(2)
        a = self.driver.window_handles
        self.driver.switch_to.window(a[-1])
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[1]/img").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[2]/div/div[3]/ul/li[7]/img").click()
        time.sleep(3)
        return self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/img').get_attribute("src")
    def sctx(self,username,pwd):
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(pwd)
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='submit']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[1]/img").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div[2]/div[2]/div/div[4]/form/div[2]/label').click()
        # 使用pywinauto来选择文件
        app = pywinauto.Desktop()
        # 选择文件上传的窗口
        dlg = app["打开"]
        dlg.print_control_identifiers()
        # 选择文件地址输入框，点击激活
        dlg["Toolbar3"].click()
        # 键盘输入上传文件的路径
        send_keys("E:\\")
        time.sleep(1)
        # 键盘输入回车，打开该路径
        send_keys("{VK_RETURN}")
        # 选中文件名输入框，输入文件名
        dlg["文件名(&N):Edit"].type_keys("01.png")
        time.sleep(1)
        # 点击打开
        dlg["打开(&O)"].click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/div/div[4]/button').click()
        time.sleep(2)
        loc = self.driver.find_element(By.XPATH, '/html/body/div[7]/div[2]')
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(loc).perform()
        message = self.driver.find_element(By.XPATH, '/html/body/div[7]/div[2]').text
        self.driver.quit()
        return message
    def outxt(self,username,pwd):
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(pwd)
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='submit']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/a[2]/img").click()
# c=Head_Sculpture_Operation()
# c.xgtx("cll","admin")