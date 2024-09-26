import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from App.pages.loginpage import LoginPage

service = Service("C:\\Users\\acer\\Python\\Python312\\chromedriver-win64\\chromedriver.exe")


class TestLogin(unittest.TestCase):
  
  @classmethod
  def setUpClass(cls):
    cls.driver = webdriver.Chrome(service=service)
    cls.driver.maximize_window()
    cls.driver.implicitly_wait(20)
    
    cls.driver.get("http://localhost:5173/")
  
  def test_login_valid(self):
    self.driver.get("http://localhost:5173/")

    driver = self.driver
    login = LoginPage(driver)
    
    login.Email('manica.kasula@fleetpanda.com')
    login.Password('Test@123')
    login.SeePass()
    login.ButtonLogin()
    login.Verify_Login()
    
    time.sleep(2)
    
  def test_not_valid(self):
    self.driver.get("http://localhost:5173/")

    driver = self.driver
    
    login = LoginPage(driver)
    
    login.Invalid_Email("abc@gmail.com")
    login.Invalid_Password("123sg#")
    login.ButtonLogin()
    login.Verify_Invalid()
    
    time.sleep(2)
    
  
  @classmethod
  def test_tearDown(cls):
    cls.driver.close()
    cls.driver.quit()


if __name__ == '__main__':
  unittest.main()
