from selenium.webdriver.common.by import By

class HomePage():
    toolList = (By.CSS_SELECTOR, '.container > .card')
    toolNames = (By.CSS_SELECTOR, '.card-title')
    toolPrices = (By.XPATH, "//span[@data-test='product-price']")

    def __init__(self, driver):
        self.driver = driver

    def getToolContainerElement(self):
        return HomePage.toolList

    def getToolList(self):
        return self.driver.find_elements(*HomePage.toolList)
    
    def getToolNames(self):
        return self.driver.find_elements(*HomePage.toolNames)
    
    def getToolPrices(self):
        return self.driver.find_elements(*HomePage.toolPrices)

