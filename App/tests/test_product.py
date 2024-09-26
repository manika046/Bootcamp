import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from App.pages.ProductPage import ProductPage
from App.tests.test_login import *

service = Service("C:\\Users\\acer\\Python\\Python312\\chromedriver.exe")


class TestProduct(TestLogin):
  
  @classmethod
  def setUpClass(cls):
    TestLogin.setUpClass()
    # cls.driver = webdriver.Chrome(service=service)
    # cls.driver.maximize_window()
    # cls.driver.implicitly_wait(20)
    #
    # cls.driver.get("http://localhost:5174")
  
  def test_create_product(self):
    self.test_valid_login()
    driver = self.driver
    
    createproduct = ProductPage(driver)
    
    createproduct.Product()
    createproduct.CreateNew()
    createproduct.ProductName("Petrol")
    createproduct.ProductCategory(" Petrol")
    createproduct.ProductStatus("available")
    createproduct.ProductUnit("gallons")
    createproduct.SaveProduct()
    createproduct.Toast_Verify()
    
  @classmethod
  def tearDown(cls):
    cls.driver.close()
    cls.driver.quit()
    

if __name__ == '__main__':
  unittest.main()