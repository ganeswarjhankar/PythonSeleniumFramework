from selenium.webdriver.common.by import By

from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# Child Class inheritance Concept applied here
# @pytest.mark.usefixtures("setup")
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.wait import WebDriverWait
# from PageObjects.CheckoutPage import CheckOutPage


class TestOne(BaseClass):

    def test_e2e(self):
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        # Click is  handled in the line after this for Checkout page
        # Nomore required the checkOutPage
        # checkOutPage = CheckOutPage(self.driver)
        # checkOutPage = homePage.shopItems()
        # .click()
        # checkOutPage = CheckOutPage(self.driver)
        cards = checkoutpage.getCardTitles()
        # cards = self.driver.find_elements(By.CSS_SELECTOR,".card-title a")
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()

            # self.driver(By.CSS_SELECTOR,".card-footer button")
        self.driver.find_element(By.CSS_SELECTOR("a[class*='btn-primary']")).click()
        confirmPage = checkoutpage.checkOutItems()
        # .click()
        # self.driver.find_element(By.XPATH, "//button[@class = 'btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        # time.sleep
        self.verifyLinkPresence("India")

        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class='alert-success']").text
        assert ("Success! Thank you!" in textMatch)
