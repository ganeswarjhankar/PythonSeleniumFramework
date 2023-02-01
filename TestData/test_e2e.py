import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from PageObjects.HomePage0 import HomePage0
from PageObjects.HomePage2 import HomePage2
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self,getData):
        log  = self.getLogger()
        homepage = HomePage0(self.driver)
        homepage.FreeItems().click()
        log.info("Click of link one")
        #self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/a").click()
        self.driver.implicitly_wait(2)



        #self.driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("test GJ ")
        homepageforms = HomePage2(self.driver)
        homepageforms.getleadname().send_keys(getData[0])



        self.driver.implicitly_wait(2)
    #self.driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000000100")
        homepageforms.getcontactnum2().send_keys(getData[1])

        self.driver.implicitly_wait(2)
    #self.driver.find_element(By.XPATH, "//*[@id='leadcity2']").send_keys("Gurugram")
        homepageforms.getleadcity2().send_keys(getData[2])
        self.driver.implicitly_wait(2)
    #self.driver.find_element(By.XPATH, "//*[@id='treamentcondition1']").send_keys("Tips Procedure")
        homepageforms.gettreamentcondition1().send_keys(getData[3])
        self.driver.implicitly_wait(2)
    #self.driver.find_element(By.XPATH, "//*[@id='leadquery']").send_keys("Test Query check")
        homepageforms.getleadquery().send_keys(getData[4])
        self.driver.implicitly_wait(2)
    #self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitNewHome']").click()
        homepageforms.getLeadSubmitNewHome().click()
        #print("BookAppointmentForm1 passed")
        #alertText  = homepageforms.getSuccessMessage().text
        self.driver.refresh()

    @pytest.fixture(params=[("TestGJ","1000000100","Gurugram","Tips Procedure","Test Query check")])
    def getData(self,request):
        return request.param

