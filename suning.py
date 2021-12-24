from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
chromedriver=webdriver.Chrome()
try:
    chromedriver.get("https://www.suning.com/")
    chromedriver.maximize_window()
    time.sleep(1)
except:
    print("没有访问到该地址！！")
try:
    # chromedriver.find_element(By.ID,'searchKeywords').send_keys("手机")
    #鼠标悬浮：
    move=chromedriver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div/ul/li[1]/a[1]')
    ActionChains(chromedriver).move_to_element(move).perform()
    time.sleep(3)
    chromedriver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div/ul/li[1]/a[1]').click()
except:
    print("无法定位输入框的！！")
a=chromedriver.window_handles
chromedriver.switch_to.window(a[-1])
try:
    chromedriver.find_element(By.XPATH,'/html/body/div[6]/div[2]/ul/li[1]').click()
except:
    print("定位手机元素错误！！！")
a=chromedriver.window_handles
chromedriver.switch_to.window(a[-1])
try:
    chromedriver.find_element(By.ID,'addCart').click()
except:
    print("添加购物车失败！！")
    chromedriver.save_screenshot("shibai.png")
else:
    print("添加购物车成功！！")
    chromedriver.save_screenshot("tjcg.png")
time.sleep(10)
chromedriver.quit()
#方法一：没有鼠标悬浮，直接搜索手机进行添加
# try:
#     chromedriver.find_element(By.ID,'searchSubmit').click()
# except:
#     print("定位搜索按钮失败！！")
# try:
#     chromedriver.find_element(By.ID,'0000000000-12313015493').click()
# except:
#     print("定位手机元素失败！！")
# a=chromedriver.window_handles
# chromedriver.switch_to.window(a[-1])
# try:
#     chromedriver.find_element(By.ID,'addCart').click()
# except:
#     print("添加购物车失败！！")
#     chromedriver.save_screenshot("shibai.png")
# else:
#     print("添加购物车成功！！")
#     chromedriver.save_screenshot("tjcg.png")
# time.sleep(10)
# chromedriver.quit()