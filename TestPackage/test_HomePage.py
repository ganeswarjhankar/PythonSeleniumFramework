# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
import pytest

from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


#class TestHomepage(BaseClass):
 #   def test_formSubmission(self, getData):
  #      homepage = HomePage(self.driver)
        # homepage.getName().send_keys("Rahul")
   #     homepage.getName().send_keys(getData["firstname"])
        # homepage.getEmail().send_keys("shetty")
    #    homepage.getEmail().send_keys(getData["lastname"])

     #   homepage.getCheckbox().click()
        # homepage.getSuccessMessage().text
        # homepage.password().send_keys("Yes")
        # S = Service("d:/chromedriver.exe")
        # driver = webdriver.Chrome(service=S)
        # driver.get("https://www.rahulshettyacademy.com/angularpractice/")
        # driver.maximize_window()
        # driver.find_element(By.CSS_SELECTOR,"[name='name']").send_keys("Rahul")
        # driver.find_element(By.XPATH,"//input[@name='email']").send_keys("Shetty")
        # driver.find_element(By.XPATH,"//input[@id='exampleInputPassword1']").send_keys("Password")
        # sel = Select(driver.find_element(By.XPATH,"//select[@id='exampleFormControlSelect1']"))
        # sel = Select(homepage.getGender())
        # self.selectOptionsByText(homepage.getGender(),"Male")
      #  self.selectOptionsByText(homepage.getGender(),getData["gender"])
        # sel.select_by_visible_text("Male")
       # homepage.submitForm().click()
        # driver.find_element(By.XPATH,"success message").click()
        # alertText = driver.find_element(By.CSS_SELECTOR,"[class*='alert-success']").text
        #alertText = homepage.getSuccessMessage().text

        #assert ("Success" in alertText)
        #self.driver.refresh()

    # datadriven Test data creation, needed to make the test not static but as dynamic
    # @pytest.fixture(params=[("Rahul", "Shetty", "Male"), ("Anushka", "Shetty", "Female")])
    #@pytest.fixture(params=[{"firstname": "Rahul", "lastname": "Shetty", "gender": "Male"},
                          #  {"firstname": "Anushka", "lastname": "Shetty", "gender": "Female"}])
    #def getData(self, request):
     #   return request.param


#################################################Original codes##############################

class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage= HomePage(self.driver)
        log.info("first name is "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param