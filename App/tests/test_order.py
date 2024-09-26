import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from App.pages.OrderPage import OrderPage
from App.tests.test_login import *


class TestOrder(TestLogin):
  
  @classmethod
  def setUpClass(cls):
    TestLogin.setUpClass()
    # cls.driver = webdriver.Chrome(service=service)
    # cls.driver.maximize_window()
    # cls.driver.implicitly_wait(20)
    #
    # cls.driver.get("http://localhost:5174")
    
  def test_create_recurring(self):
    self.test_valid_login()
    driver = self.driver
    Order = OrderPage(driver)
    
    Order.CreateNew()
    # Order.Verify_Text()
    Order.Customer("Himal Lubricants Pvt.Ltd")
    Order.Next_Select()
    Order.Branch("Himal Lubricants Pvt.Ltd B1")
    # Order.Location("Bhaktapur, Nepal")
    Order.Delivery()
    Order.Bulk_delivery("Premium LPG - gallons")
    Order.Click()
    Order.Quantity(50)
    Order.Recurring()
    # Order.Start_Recurrence()
    Order.Frequency("every_week")
    # Order.End_Recurrence("09-30-2024T11:06AM")
    Order.Driver("Rajesh Rawani")
    Order.Category("Wagon")
    Order.CreateOrder()
    Order.Toast_Verify()
    
    time.sleep(10)
  
  @classmethod
  def tearDown(cls):
    cls.driver.close()
    cls.driver.quit()
    

if __name__ == '__main__':
  unittest.main()