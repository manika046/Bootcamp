import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from App.pages.Assetpage import AssetPage
from App.tests.test_login import *


class TestAsset(TestLogin):
  
  @classmethod
  def setUpClass(cls):
    TestLogin.setUpClass()
  
  def test_create_asset(self):
    self.test_login_valid()
    driver = self.driver
    create_asset = AssetPage(driver)
    
    create_asset.AssetButton()
    create_asset.VerifyAssetClick()
    create_asset.CreateNew()
    create_asset.Clicked_Verify()
    create_asset.AssetId("BA KHA 2114")
    create_asset.AssetCategory("Truck")
    create_asset.AssetStatus("active")
    create_asset.SaveButton()
    create_asset.Toast_Verify()
    time.sleep(10)
    
  def test_edit_asset(self):
    self.test_create_asset()
    driver = self.driver
    
    edit_asset = AssetPage(driver)
    edit_asset.EditAsset()
    edit_asset.EditStatus("active")
    edit_asset.EditSave()
    edit_asset.Update_Verify()
  
  @classmethod
  def test_tearDown(cls):
    cls.driver.close()
    cls.driver.quit()


if __name__ == '__main__':
  unittest.main()