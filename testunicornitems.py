import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Chrome()
driver.maximize_window()


class TestUnicorn(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()


    def testlogIn(self):
        driver = self.driver
        driver.get("http://unicornitems.com/my-account/")
        #WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located(By.NAME,"username"))
        element_username = driver.find_element(By.NAME,"username")
        element_password = driver.find_element(By.NAME,"password")

        element_username.send_keys("1")
        element_password.send_keys("1")

        button_login = driver.find_element(By.NAME,"login")
        button_login.click()
        WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div[3]/div/div/article/div/div/div[1]/div[1]/ul")))

        alert = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div/article/div/div/div[1]/div[1]/ul")
        assert "ERROR" in alert.text

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
