from distutils.spawn import find_executable
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.implicitly_wait(20)

driver.get('https://www.baidu.com/')
driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys('lol\n')
driver.find_element(By.XPATH,'//*[@id="1"]/h3/a[1]').click()
time.wait(5)
driver.find_element(By.LINK_TEXT,'查看详情').click()











