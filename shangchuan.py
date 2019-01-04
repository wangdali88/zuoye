from selenium  import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_css_selector('span [class="soutu-btn"]').click()
driver.find_element_by_css_selector('input[type="file"]').send_keys('C:\\Users\\Public\\Pictures\\Sample Pictures\\baxianhua.jpg')

time.sleep(10)

driver.quit()