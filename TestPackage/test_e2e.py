from selenium.webdriver.common.by import By

from PageObjects.HomePage import HomePage

#########################original imports###########################

#from pageObjects.CheckoutPage import CheckOutPage
# from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

import time
###############################################################END#########################################


# Child Class inheritance Concept applied here
# @pytest.mark.usefixtures("setup")
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.wait import WebDriverWait
# from PageObjects.CheckoutPage import CheckOutPage


# class TestOne(BaseClass):

# def test_e2e(self):
# homePage = HomePage(self.driver)
# checkoutpage = homePage.shopItems()
# Click is  handled in the line after this for Checkout page
# Nomore required the checkOutPage
# checkOutPage = CheckOutPage(self.driver)
# checkOutPage = homePage.shopItems()
# .click()
# checkOutPage = CheckOutPage(self.driver)
# cards = checkoutpage.getCardTitles()
# cards = self.driver.find_elements(By.CSS_SELECTOR,".card-title a")
# i = -1
# for card in cards:
#    i = i + 1
#   cardText = card.text
#  print(cardText)
#   if cardText == "Blackberry":
#      checkoutpage.getCardFooter()[i].click()

# self.driver(By.CSS_SELECTOR,".card-footer button")
# self.driver.find_element(By.CSS_SELECTOR("a[class*='btn-primary']")).click()
# confirmPage = checkoutpage.checkOutItems()
# .click()
# self.driver.find_element(By.XPATH, "//button[@class = 'btn btn-success']").click()
# self.driver.find_element(By.ID, "country").send_keys("ind")
# time.sleep
# self.verifyLinkPresence("India")

# self.driver.find_element(By.LINK_TEXT, "India").click()
# self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
# self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
# textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class='alert-success']").text
# assert ("Success! Thank you!" in textMatch)


#########################original codes from udemy####################


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        log.info("getting all the card titles")
        cards = checkoutpage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()

        self.driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()

        confirmpage = checkoutpage.checkOutItems()
        log.info("Entering country name as ind")
        self.driver.find_element(By.ID,"country").send_keys("ind")
        # time.sleep(5)
        self.verifyLinkPresence("India")
        #time.sleep(2)

        self.driver.find_element(By.LINK_TEXT,'India').click()
        self.driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
        # self.driver.find_element_by_xpath("//input[@type='submit']").click()
        self.driver.find_element(By.XPATH ,"//input[@type='submit']").click()
        #self.driver.find_element_by_css_selector("[type='submit']").click()
        textMatch = self.driver.find_element(By.CSS_SELECTOR,"[class*='alert-success']").text

        log.info("Text received from application is " + textMatch)

        assert ("Success! Thank you!" in textMatch)
