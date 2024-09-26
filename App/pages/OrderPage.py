import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class Locator:
  # # order
  dark = "//*[@id='root']/div/div[1]/div/button"
  select_order = "//*[@id='field-:r6:]"
  create_new = "//*[@id='root']/div/div[2]/div[1]/div/button[1]"
  select_customer = "/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[1]/div/div/select"
  next_branch = "/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[1]/button"
  select_branch = "/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[2]/div[1]/div/select"
  location = "/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[2]/div[2]/div/select"
  next_delivery_details = "/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[2]/button[2]"
  # select
  bulk_delivery = "/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[3]/div[2]/div[1]/div/select"
  # for recurring order modal
  recurring_delivery = "/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[3]/div[2]/div[2]/label/span"
  start_recurrence = "//*[@id='field-:r3m:']"
  # select
  select_frequency = "/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[3]/div[2]/div[2]/div[2]/div/select"
  end_recurrence = "/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[3]/div[2]/div[2]/div[3]/input"
  # select
  assign_driver = "/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[3]/div[3]/div[1]/div/div/select"
  # select
  asset_category = "/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[3]/div[3]/div[2]/div/div/select"
  plan_date = "//*[@id='field-:r3c:']"
  create_order = "/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[3]/button[2]"


class OrderPage():
  def __init__(self, driver):
    self.driver = driver
    
    self.dark_mode = Locator.dark
    self.create_new = Locator.create_new
    self.verify = "//*[@id='chakra-modal--header-:rd:']"
    self.select_customer = Locator.select_customer
    self.next_branch = Locator.next_branch
    self.select_branch = Locator.select_branch
    self.location = Locator.location
    self.select_delivery_details = Locator.next_delivery_details
    self.bulk_delivery = Locator.bulk_delivery
    self.click_checkbox = "/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/label/span[1]"
    self.quantity = "/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/input"
    self.recurring_delivery = Locator.recurring_delivery
    self.start_recurrence = Locator.start_recurrence
    self.select_frequency = Locator.select_frequency
    self.end_recurrence = Locator.end_recurrence
    self.assign_driver = Locator.assign_driver
    self.asset_category = Locator.asset_category
    self.plan_date = Locator.plan_date
    self.create_order = Locator.create_order
  
  def DarkMode(self):
    self.driver.find_element(By.XPATH, self.dark_mode).click()
  
  def CreateNew(self):
    self.driver.find_element(By.XPATH, self.create_new).click()
    time.sleep(2)
  
  def Verify_Text(self):
    # self.driver.switch_to.window(self.driver.current_window_handle)
    self.driver.implicitly_wait(20)
    # print(self.driver.current_url)
    # modal_element = WebDriverWait(self.driver, 10).until(
    #   EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div/section"))
    # )
    # self.driver.switch_to.active_element = modal_element
    # modal_container = self.driver.find_element(By.CLASS_NAME, "chakra-modal__content css-pv22qu")
    #
    # self.driver.switch_to.frame(modal_container)
    # self.driver.switch_to.window(modal_container.window_handle)
    try:
      element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, self.verify))
      )
      assert element.text == "Create Delivery Order"
      print("Create Order! ")
    
    except:
      print("Sorry You Didn't Get! ")
  
  def Customer(self, customer):
    Select(self.driver.find_element(By.XPATH, self.select_customer)).select_by_value(customer)
    time.sleep(2)
  
  def Next_Select(self):
    self.driver.find_element(By.XPATH, self.next_branch).click()
    time.sleep(1)
  
  def Branch(self, branch):
    Select(self.driver.find_element(By.XPATH, self.select_branch)).select_by_value(branch)
    time.sleep(1)
  
  def Location(self, location):
    Select(self.driver.find_element(By.XPATH, self.location)).select_by_value(location)
    time.sleep(1)
  
  def Delivery(self):
    self.driver.find_element(By.XPATH, self.select_delivery_details).click()
    time.sleep(1)
  
  def Bulk_delivery(self, bulk):
    Select(self.driver.find_element(By.XPATH, self.bulk_delivery)).select_by_visible_text(bulk)
  
  def Click(self):
    self.driver.find_element(By.XPATH, self.click_checkbox).click()
  
  def Quantity(self, quantity):
    self.driver.find_element(By.XPATH, self.quantity).send_keys(quantity)
  
  def Recurring(self):
    self.driver.find_element(By.XPATH, self.recurring_delivery).click()
  
  def Frequency(self, frequency):
    Select(self.driver.find_element(By.XPATH, self.select_frequency)).select_by_value(frequency)
  
  def End_Recurrence(self, date):
    self.driver.find_element(By.XPATH, self.end_recurrence).send_keys(date)
  
  def Driver(self, driver):
    Select(self.driver.find_element(By.XPATH, self.assign_driver)).select_by_value(driver)
  
  def Category(self, category):
    Select(self.driver.find_element(By.XPATH, self.asset_category)).select_by_value(category)
  
  def CreateOrder(self):
    self.driver.find_element(By.XPATH, self.create_order).click()
    
  def Toast_Verify(self):
    try:
      toast_message_element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/div/div[1]/div[2]"))
      )
      
      toast_message_text = toast_message_element.text
      
      assert toast_message_text == "Order Created"
      print("Order Created")
    
    except Exception as e:
      print("Failed to verify toast message: {str(e)}")