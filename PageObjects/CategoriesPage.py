from selenium.webdriver.common.by import By
from PageObjects.HomePage import HomePage
from PageObjects.ProductPage import ProductPage

# Inheriting from both HomePage and ProductPage
class Category(HomePage, ProductPage):

    headingText = (By.CSS_SELECTOR, 'h2[data-test]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Returns the heading text according to the 'category' parameter, 'Hand Tools' or 'Power Tools'
    def getHeading(self, category):
        if category == 'Hand Tools':
            self.selectHandTools()
        elif category == 'Power Tools':
            self.selectPowerTools()
        return self.driver.find_element(*Category.headingText).text
    