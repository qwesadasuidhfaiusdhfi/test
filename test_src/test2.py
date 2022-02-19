from re import X
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#wd = webdriver.Chrome()

#wd.get('http://cdn1.python3.vip/files/selenium/sample2.html')


# 先根据name属性值 'innerFrame'，切换到iframe中
""" wd.switch_to.frame('innerFrame')

# 根据 class name 选择元素，返回的是 一个列表
elements = wd.find_elements(By.CLASS_NAME, 'plant')

for element in elements:
    print(element.text)

# 切换回 最外部的 HTML 中
wd.switch_to.default_content()

# 然后再 选择操作 外部的 HTML 中 的元素
wd.find_element_by_id('outerbutton').click()
time.sleep(5)
wd.quit() """
options = webdriver.ChromeOptions()
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])

wd = webdriver.Chrome(options=options) 

wd.implicitly_wait(10)#d最大等待时间 每隔半秒检查一次

wd.get('https://www.baidu.com')
wd.find_element(By.XPATH,'//*[@id="kw"]').send_keys('lol\n')
wd.find_element(By.XPATH,'//*[@id="1"]/h3/a[1]').click()


# wd.title属性是当前窗口的标题栏 文本


for handle in wd.window_handles:
    # 先切换到该窗口
   
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if '英雄联盟' in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break
wd.find_element(By.XPATH,'//*[@id="J_headNav"]/li[1]/a/span[1]').click()
mainWindow = wd.current_window_handle
for handle in wd.window_handles:
    # 先切换到该窗口
    
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if '攻略中心-英雄联盟官方网站-腾讯游戏' in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div/div/ul/li[2]/a').click()

wd.switch_to.window(mainWindow)
wd.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/p[1]/a').click()
iframe=wd.find_element(By.XPATH,'//*[@id="loginIframe"]')
wd.switch_to.frame(iframe)
wd.find_element(By.XPATH,'//*[@id="switcher_plogin"]').click()
wd.find_element(By.XPATH,'//*[@id="u"]').send_keys('2939656896')
wd.find_element(By.XPATH,'//*[@id="p"]').send_keys('666162636')
time.sleep(2)
wd.find_element(By.XPATH,'//*[@id="login_button"]').click()

