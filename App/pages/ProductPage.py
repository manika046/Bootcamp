import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class Locators:
  product_button = "/html/body/div[1]/div/div[1]/div/nav/a[2]"
  create_new = "/html/body/div[1]/div/div[2]/div[1]/div/button"
  product_name = "/html/body/div[3]/div[3]/div/section/div/div[1]/input"
  product_category = "/html/body/div[3]/div[3]/div/section/div/div[2]/div/select"
  product_status = "/html/body/div[3]/div[3]/div/section/div/div[3]/div/select"
  product_unit = "/html/body/div[3]/div[3]/div/section/div/div[4]/div/select"
  save_product = "/html/body/div[3]/div[3]/div/section/footer/button[1]"


class ProductPage():
  def __init__(self, driver):
    self.driver = driver
    
    self.product_button = Locators.product_button
    self.create_new = Locators.create_new
    self.product_name = Locators.product_name
    # select
    self.product_category = Locators.product_category
    self.product_status = Locators.product_status
    self.product_unit = Locators.product_unit
    self.save_product = Locators.save_product
  
  def Product(self):
    self.driver.find_element(By.XPATH, self.product_button).click()
    time.sleep(1)
  
  def CreateNew(self):
    self.driver.find_element(By.XPATH, self.create_new).click()
    time.sleep(1)
  
  def ProductName(self, name):
    self.driver.find_element(By.XPATH, self.product_name).send_keys(name)
    time.sleep(1)
  
  def ProductCategory(self, category):
    Select(self.driver.find_element(By.XPATH, self.product_category)).select_by_value(category)
    time.sleep(1)
  
  def ProductStatus(self, status):
    Select(self.driver.find_element(By.XPATH, self.product_status)).select_by_value(status)
    time.sleep(1)

  def ProductUnit(self, unit):
    Select(self.driver.find_element(By.XPATH, self.product_unit)).select_by_value(unit)
    time.sleep(1)
    
  def SaveProduct(self):
    self.driver.find_element(By.XPATH, self.save_product).click()

  def Toast_Verify(self):
    try:
      toast_message_element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/div/div[1]/div[2]"))
      )
      
      toast_message_text = toast_message_element.text
      
      assert toast_message_text == "Product Created"
      print("Product Created")
    
    except Exception as e:
      print("Failed to verify toast message: {str(e)}")
      
    time.sleep(2)
