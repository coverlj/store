from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import By
import time


url = "127.0.0.1:4723/wd/hub"


param = {
  "deviceName": "127.0.0.1:62001",
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "appPackage": "com.ss.android.ugc.aweme",
  "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity"
}
driver =  webdriver.Remote(url,param)
time.sleep(10)
driver.find_element(By.ID,"com.ss.android.ugc.aweme:id/bdb").click()
while True:
    TouchAction(driver).press(x=379,y=868).move_to(x=333,y=236).release().perform()
    time.sleep(20)





















