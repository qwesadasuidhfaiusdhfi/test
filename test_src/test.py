from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])

wd = webdriver.Chrome(options=options) 

wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')

# 根据属性选择元素
element = wd.find_element(By.CSS_SELECTOR, '[href="http://www.miitbeian.gov.cn"]')

""" a[href*="miitbeian"] href中包含的
a[href^="http"] 以这个开头
a[href$="gov.cn"] 以这个结尾""" 
#CSS 选择器 可以指定 选择的元素要 同时具有多个属性的限制，像这样 div[class=misc][ctype=gun]
# 打印出元素对应的html
#找子元素或者后代 > or ' '
#，代表选择全部
#切换文档wd.switch_to.frame(frame_reference) 其中， frame_reference 可以是 frame 元素的属性 name 或者 ID 。
#wd.switch_to.frame(wd.find_element(By.TAG_NAME, "iframe"))
print(element.get_attribute('outerHTML'))