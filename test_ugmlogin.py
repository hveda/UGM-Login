import unittest  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
from config import ugm_username, ugm_password  
  
class UGMLoginTest(unittest.TestCase):  
    def setUp(self):  
        chrome_options = Options()  
        chrome_options.add_argument("--headless")  
        self.driver = webdriver.Chrome(options=chrome_options)  
        self.driver.set_window_size(800, 600)  
  
    def test_login(self):  
        driver = self.driver  
        driver.get('https://internet.ugm.ac.id/sso/login')  
  
        email = driver.find_element_by_id("username")  
        email.send_keys(ugm_username)  
  
        password = driver.find_element_by_id("password")  
        password.send_keys(ugm_password)  
  
        loginBtn = driver.find_element_by_name("submit")  
        loginBtn.click()  
  
        # Add assertions here to verify the login process  
  
    def tearDown(self):  
        self.driver.quit()  
  
if __name__ == "__main__":  
    unittest.main()  

