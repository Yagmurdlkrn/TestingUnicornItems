import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.maximize_window()


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()


    def testlogIn(self):
        driver = self.driver
        driver.get("http://unicornitems.com/my-account/")
        element_username = driver.find_element(By.NAME,"username")
        element_username.send_keys("1")
        element_password = driver.find_element(By.NAME,"password")
        element_password.send_keys("1")
        button_login = driver.find_element(By.NAME,"login")
        button_login.click()
        assert "ERROR: INCORRECT USERNAME OR PASSWORD." in driver.page_source

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
