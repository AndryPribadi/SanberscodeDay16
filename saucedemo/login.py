import unittest
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        

    def test_failed_login_with_fail_username(self): #test cases 1
        # steps
        driver = self.browser #buka web browser
        driver.get("http://www.saucedemo.com/") # buka situs
        driver.find_element(By.ID,"user-name").send_keys("haitest") # ketik nama
        driver.find_element(By.NAME, "login-button").click()
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        self.assertIn("Epic sadface: Password is required", error_message)

    def test_failed_login_with_empty_password(self): #test cases 2
        # steps
        driver = self.browser #buka web browser
        driver.get("http://www.saucedemo.com/") # buka situs
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # ketik nama
        driver.find_element(By.ID,"password").send_keys("") # ketik password kosong
        driver.find_element(By.NAME, "login-button").click()
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        self.assertIn("Epic sadface: Password is required", error_message)

    def test_success_login(self): #test cases 3
        # steps
        driver = self.browser #buka web browser
        driver.get("http://www.saucedemo.com/") # buka situs
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # ketik nama
        driver.find_element(By.CSS_SELECTOR,"[data-test='password']").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()

    

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()