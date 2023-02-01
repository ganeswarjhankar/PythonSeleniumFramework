from selenium.webdriver.common.by import By


class HomePage0:
    def __init__(self,driver):
        self.driver = driver

    Free = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/a")


    def FreeItems(self):
        return self.driver.find_element(*HomePage0.Free)




