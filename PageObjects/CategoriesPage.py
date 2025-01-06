from selenium.webdriver.common.by import By
from PageObjects.HomePage import HomePage

class Category(HomePage):

    headingText = (By.CSS_SELECTOR, 'h2[data-test]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def getHeading(self, category):
        if category == 'Hand Tools':
            self.selectHandTools()
        elif category == 'Power Tools':
            self.selectPowerTools()
        return self.driver.find_element(*Category.headingText).text
    