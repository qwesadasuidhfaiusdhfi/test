from gettext import find
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)    # Chrome浏览器 打开的是一个webdriver类型的对象 可以看成是浏览器的一个操控界面 



# 打开网页
driver.get("http://www.baidu.com") # 打开url网页 比如 driver.get("http://www.baidu.com")
driver.implicitly_wait(10)#如果找不到元素， 每隔半秒钟再去界面上查看一次， 直到找到该元素， 或者 过了10秒 最大时长。
element = driver.find_element(By.ID, 'kw')
#element.clear() # 清除输入框已有的字符串
print(element.get_attribute('class'))#获取元素的属性
driver.find_element(By.ID, 'kw').send_keys('教育\n')#在输入框中输入字符串
driver.find_element(By.CSS_SELECTOR,)
"""
使用了 WebDriver 对象 的方法 find_element ，

这行代码运行是，就会发起一个请求通过 浏览器驱动 转发给浏览器，告诉它，需要选择一个id为 kw 的元素。

浏览器，找到id为kw的元素后，将结果通过 浏览器驱动 返回给 自动化程序， 所以 find_element 方法会 返回一个 WebElement 类型的对象。

这个WebElement 对象可以看成是对应 页面元素 的遥控器。

我们通过这个WebElement对象，就可以 操控 对应的界面元素。

调用这个对象的 send_keys 方法就可以在对应的元素中 输入字符串，

调用这个对象的 click 方法就可以 点击 该元素。"""
""" wd.find_element(By.ID, 'username').send_keys('byhy')
wd.find_element(By.CLASS_NAME, 'password').send_keys('sdfsdf')
wd.find_element(By.TAG_NAME, 'input').send_keys('sdfsdf')
wd.find_element(By.CSS_SELECTOR,'button[type=submit]').click() """
""" 
我们可以把 id 想象成元素的编号， 是用来在html中标记该元素的。 根据规范， 如果元素有id属性 ，这个id 必须是当前html中唯一的。

所以如果元素有id， 根据id选择元素是最简单高效的方式。 """
#tag class id
#tag 例如div 
# 根据 tag名 选择元素的 CSS Selector 语法非常简单，直接写上tag名即可 
# elements = wd.find_elements(By.CSS_SELECTOR, 'div')
#根据id属性 选择元素的语法是在id号前面加上一个井号： #id值
#  element = wd.find_element(By.CSS_SELECTOR, '#searchtext')
#根据class属性 选择元素的语法是在 class 值 前面加上一个点：
#  elements = wd.find_elements(By.CSS_SELECTOR, '.animal')



