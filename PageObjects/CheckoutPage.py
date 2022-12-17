from selenium.webdriver.common.by import By
from PageObjects.ConfirmPage import ConfirmPage


# from PageObjects.CheckoutPage import CheckOutPage

class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, "  .card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    # cards = self.driver(By.CSS_SELECTOR,".card-title a")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    # Successfully created a pageObject GetCardTitle

    def getCardFooter(self):
        return self.driver.find_element(CheckOutPage.cardFooter)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
