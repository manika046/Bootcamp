import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Locator:
  email_id = "//*[@id='email']"
  password_id = "//*[@id='password']"
  password_see = "/html/body/div[1]/div/div/form/div/div[2]/div/div/button"
  login_button = "/html/body/div[1]/div/div/form/div/button"
  dashboard_check = "//*[@id='root']/div/div[1]/div/a/div"
  invalid_txt = "//*[@id='root']/div/div/p"

class LoginPage:
  
  def __init__(self, driver):
    self.driver = driver
    
    self.email_textbox = Locator.email_id
    self.password_textbox = Locator.password_id
    self.pass_see = Locator.password_see
    self.button_login = Locator.login_button
    self.valid_login = Locator.dashboard_check
    self.invalid = Locator.invalid_txt
  
  def Email(self, email):
    self.driver.find_element(By.XPATH, self.email_textbox).send_keys(email)
    time.sleep(1)
  
  def Password(self, password):
    self.driver.find_element(By.XPATH, self.password_textbox).send_keys(password)
    time.sleep(1)
  
  def SeePass(self):
    self.driver.find_element(By.XPATH, self.pass_see).click()
    time.sleep(2)
  
  def ButtonLogin(self):
    self.driver.find_element(By.XPATH, self.button_login).click()
    time.sleep(2)
  
  def Verify_Login(self):
    try:
      element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, self.valid_login))
      )
      assert element.text == "Dashboard"
      print("Successfully Login! ")
      
    except:
      print("Sorry You Didn't Logged In! ")
  
  def Invalid_Email(self, iemail):
    self.driver.find_element(By.XPATH, self.email_textbox).send_keys(iemail)
  
  def Invalid_Password(self, ipassword):
    self.driver.find_element(By.XPATH, self.password_textbox).send_keys(ipassword)
  
  def Verify_Invalid(self):
    try:
      element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, self.invalid))
      )
      assert element.text == "Invalid email or password!"
      print("Invalid Email or Password")
    
    except Exception as e:
      print(f"Exception occurred: {e}")