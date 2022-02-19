from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.implicitly_wait(20)
driver.get('http://baidu.com')
element = driver.find_element(By.name,"source")
target = driver.find_element(By.name,"target")

for handle in driver.window_handles:
    driver.switch_to_window(handle)
#切换窗口
driver.switch_to_default_content()
#回到原窗口
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()