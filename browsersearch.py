from selenium import webdriver
import time
def Param(url,selector,keyword):
    driver=webdriver.Chrome()
    driver.get(url)
    driver.find_element_by_id(selector).send_keys(keyword)
    
    time.sleep(3)
    driver.quit()


Param('http://www.baidu.com','kw','bing')
Param('http://www.baidu.com','kw','百度')
