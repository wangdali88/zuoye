import  unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class testcasetest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_baidu_search(self):
        driver= self.driver
        driver.get('http://www.bing.com')
        driver.find_element_by_id('sb_form_q').send_keys('hello world')
        driver.find_element_by_id('sb_form_go').send_keys(Keys.ENTER)
        time.sleep(2)


    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()