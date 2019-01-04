from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
print(driver.title)
assert "google" not in driver.title
#断言出错时，程序结束退出
driver.find_element_by_id("kw").send_keys("hello world")
driver.find_element_by_id('su').click()

time.sleep(3)


result = driver.find_element_by_id('content_left').text
print(result)
assert "hello world" in result
time.sleep(3)
driver.quit()

