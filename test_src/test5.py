
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


options = webdriver.ChromeOptions()
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])
#更改测试样例
wd=webdriver.Chrome(options=options)
time.sleep(1)
wd.get('https://lol.qq.com/main.shtml') 
ActionChains(wd).move_to_element(wd.find_element(By.XPATH,'//*[@id="J_headNav"]/li[2]/a')).perform()
time.sleep(2)
ac=ActionChains(wd)
ac.move_to_element(wd.find_element(By.XPATH,'//*[@id="J_headNavSub"]/li[2]/a[1]')).perform()
wd.find_element(By.XPATH,'//*[@id="J_headNavSub"]/li[2]/a[1]').click()
for handle in wd.window_handles:
    wd.switch_to_window(handle)
    if '腾讯游戏支付中心' in wd.title :
        break
time.sleep(1)
frame=wd.find_element(By.XPATH,'//*[@id="loginIframe"]')
wd.switch_to_frame(frame)
wd.find_element(By.XPATH,'//*[@id="switcher_plogin"]').click()
wd.find_element(By.XPATH,'//*[@id="u"]').send_keys('2939656896')
wd.find_element(By.XPATH,'//*[@id="p"]').send_keys('666162636')
time.sleep(0.5)
wd.find_element(By.XPATH,'//*[@id="login_button"]').click()
wd.get_screenshot_as_file('1.png')



