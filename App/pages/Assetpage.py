import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

class AssetPage:
  def __init__(self, driver):
    self.driver = driver
    
    self.asset_button = "/html/body/div[1]/div/div[1]/div/nav/a[1]"
    self.asset_click = "/html/body/div[1]/div/div[2]/div[1]/h2"
    self.create_new = "/html/body/div[1]/div/div[2]/div[1]/div/button"
    self.clicked = "/html/body/div[3]/div[3]/div/section/header"
    self.asset_id = "/html/body/div[3]/div[3]/div/section/div/div[1]/input"
    # select
    self.asset_category = "/html/body/div[3]/div[3]/div/section/div/div[2]/div/select"
    self.asset_status = "/html/body/div[3]/div[3]/div/section/div/div[3]/div/select"
    self.save_button = "/html/body/div[3]/div[3]/div/section/footer/button[1]"
    self.cancel_button = "/html/body/div[3]/div[3]/div/section/footer/button[2]"
    self.verify_text = "/html/body/div[1]/div/div[2]/div[3]/div/div/div[1]/div[2]"
    
    self.table = "/html/body/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div[1]/div[2]"
    self.locate_truck = "/html/body/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div[1]/div[2]/div/div[1]"
    self.edit_button = "/html/body/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div[1]/div[2]/div/div[1]/div[4]/div/button[1]"
    self.edit_status = "/html/body/div[3]/div[3]/div/section/div/div[2]/div/select"
    self.edit_save = "/html/body/div[3]/div[3]/div/section/footer/button[1]"
    self.edit_verify = "/html/body/div[1]/div/div[2]/div[3]/div/div/div[1]/div[2]"
    
  def AssetButton(self):
    self.driver.find_element(By.XPATH, self.asset_button).click()
    time.sleep(1)
    
  def VerifyAssetClick(self):
    asset = WebDriverWait(self.driver, 10).until(
      EC.visibility_of_element_located((By.XPATH, self.asset_click))
    )
    assert asset.text == "Asset List"
    print("CLICKED ASSERT! ")
    
  def CreateNew(self):
    self.driver.find_element(By.XPATH, self.create_new).click()
    
  def Clicked_Verify(self):
    try:
      element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, self.clicked))
      )
      assert element.text == "Asset Details"
      print("CLICKED CREATE NEW ASSET! ")
      
    except Exception as e:
      print("DIDN'T CLICKED! ")
    
  def AssetId(self, id):
    self.driver.find_element(By.XPATH, self.asset_id).send_keys(id)
    
  def AssetCategory(self, category):
    Select(self.driver.find_element(By.XPATH, self.asset_category)).select_by_value(category)
    time.sleep(1)
    
  def AssetStatus(self, status):
    Select(self.driver.find_element(By.XPATH, self.asset_status)).select_by_value(status)
    time.sleep(1)
    
  def SaveButton(self):
    self.driver.find_element(By.XPATH, self.save_button).click()
  
  def Toast_Verify(self):
    try:
      toast_message_element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, self.verify_text))
      )
      
      toast_message_text = toast_message_element.text
      
      assert toast_message_text == "Asset Created"
      print("ASSET CREATED! ")
    
    except Exception as e:
      print("Failed to verify toast message: {str(e)}")
      
  def EditAsset(self):
    self.driver.implicitly_wait(5)
    self.driver.find_element(By.XPATH, self.edit_button).click()
    
  def EditStatus(self, status):
    Select(self.driver.find_element(By.XPATH, self.edit_status)).select_by_value(status)
    time.sleep(1)
    
  def EditSave(self):
    self.driver.find_element(By.XPATH, self.edit_save).click()
  
  def Update_Verify(self):
    try:
      toast_message_element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, self.edit_verify))
      )
      
      toast_message_text = toast_message_element.text
      
      assert toast_message_text == "Asset Updated"
      print("ASSET UPDATED! ")
    
    except Exception as e:
      print("Failed to verify: {str(e)}")