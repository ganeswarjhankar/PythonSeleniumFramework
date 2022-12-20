#from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import CheckOutPage


#class HomePage:
    # Create Constructor to make use of Page Object Model for "Driver"
    #def __init__(self, driver):
     #   self.driver = driver

    # tuple# declared Shop Locator
    #shop = (By.CSS_SELECTOR, "a[href*='shop']")
    #name = (By.CSS_SELECTOR, "[name='name']")
    #email = (By.NAME, "email")
    #submit = (By.XPATH, "//input[@value='Submit']")
    # password = (By.XPATH,"//input[@id='exampleInputPassword1']")
    #check = (By.ID, "exampleCheck1")
    #successMessage =(By.CSS_SELECTOR, "[class*='alert-success']")
    # MaleOption = (By.XPATH,"//select[@id='exampleFormControlSelect1']")
    #Gender = (By.ID, "exampleFormControlSelect1")

    #def shopItems(self):
        # mark as star and make them deserializes as tuple
        #self.driver.find_element(*HomePage.shop).click()
        # Alt Shift enter Press to import the function
        #checkOutPage = CheckOutPage(self.driver)
        #return checkOutPage

    #def getName(self):
     #   return self.driver.find_element(*HomePage.name)

    #def getEmail(self):
    #    return self.driver.find_element(*HomePage.email)

    #def submitForm(self):
     #   return self.driver.find_element(*HomePage.shop)

    #def getCheckbox(self):
       # return self.driver.find_element(*HomePage.check)

    #def getSuccessMessage(self):
     #   return self.driver.find_element(*HomePage.successMessage)

    #def getGender(self):
      #  return self.driver.find_element(*HomePage.Gender)

        # driver.find_elements(By.XPATH, "//div[@class='card h-100']")



# Basic example of Instance Variable and Class Variable
# In the previous Clases the rahul shetty has clearly exaplained the characteristics.
# instance call self.shop- instant varaiable are part of object constructors
# class var- class.shop


###############################new code for udemy###########################
from selenium.webdriver.common.by import By

#from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender= (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)


    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)

    def SubmitForm(self):
        return self.driver.find_element(*HomePage.shop)

    #def getCheckbox(self):
      #  pass


