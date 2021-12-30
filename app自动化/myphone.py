from appium import webdriver
import time
url = "127.0.0.1:4723/wd/hub"


param = {
  "deviceName": "7181352d",
  "platformName": "Android",
  "platformVersion": "11",
  "appPackage": "com.tencent.mobileqq",
  "appActivity": "com.tencent.mobileqq.activity.SplashActivity"
}
driver =  webdriver.Remote(url,param)
time.sleep(10)
el1 =driver.find_element_by_accessibility_id("同意")
el1.click()
time.sleep(15)
el2 =driver.find_element_by_id("com.tencent.mobileqq:id/btn_login")
el2.click()
time.sleep(15)
el3 =driver.find_element_by_id("com.tencent.mobileqq:id/mr1")
el3.click()
time.sleep(15)
el4 =driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱")
el4.send_keys("2090948831")
time.sleep(15)
el5 = driver.find_element_by_accessibility_id("密码 安全")
el5.send_keys("lj123456")
time.sleep(15)
el6 =driver.find_element_by_accessibility_id("登 录")
el6.click()
time.sleep(15)
el7 =driver.find_element_by_accessibility_id("确定")
el7.click()
time.sleep(15)
















