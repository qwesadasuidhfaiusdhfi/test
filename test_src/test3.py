
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
options=webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
wd=webdriver.Chrome(options=options)
wd.get('https://www.baidu.com')
wd.implicitly_wait(10)#d最大等待时间 每隔半秒检查一次



select = Select(wd.find_element(By.ID, "ss_single"))

# 通过 Select 对象选中小雷老师
select.select_by_visible_text("小雷老师")
select=Select(wd.find_element(By.CSS_SELECTOR,'#ss_single'))
select.select_by_visible_text('小凯老师')
