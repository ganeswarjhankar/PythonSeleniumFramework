from selenium.webdriver.common.by import By


class HomePage2:

    def __init__(self,driver):
        self.driver = driver


    #self.driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("test GJ ")
    leadname = (By.XPATH, "//*[@id='leadname2']")
    contactnum2= (By.XPATH, "//*[@id='contactnum2']")
    leadcity2 = (By.XPATH, "//*[@id='leadcity2']")
    treamentcondition1 = (By.XPATH, "//*[@id='treamentcondition1']")
    leadquery = (By.XPATH, "//*[@id='leadquery']")
    LeadSubmitNewHome = (By.XPATH, "//*[@id='LeadSubmitNewHome']")

#self.driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("test GJ ")
    def getleadname(self):
        return self.driver.find_element(*HomePage2.leadname)
#self.driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("test GJ ")
    def getcontactnum2(self):
        return self.driver.find_element(*HomePage2.contactnum2)
#self.driver.find_element(By.XPATH, "//*[@id='leadcity2']").send_keys("Gurugram")
    def getleadcity2(self):
        return self.driver.find_element(*HomePage2.leadcity2)

    def gettreamentcondition1(self):
        return self.driver.find_element(*HomePage2.treamentcondition1)

    def getleadquery(self):
        return self.driver.find_element(*HomePage2.leadquery)

    def getLeadSubmitNewHome(self):
        return self.driver.find_element(*HomePage2.LeadSubmitNewHome)

    #def getSuccessMessage(self):
        #return self.driver.find_element(By.XPATH,"/html/body/div/div/div/h1")

