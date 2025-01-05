from selenium.webdriver.common.by import By
from PageObjects.ProductPage import ProductPage

class HomePage:
    toolList = (By.CSS_SELECTOR, '.container > .card')
    toolNames = (By.CSS_SELECTOR, '.card-title')
    toolPrices = (By.XPATH, "//span[@data-test='product-price']")
    individualTool = (By.CSS_SELECTOR, "a[data-test='product-{}']")


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

    def getIndividualTool(self, ID):
        toolName = self.driver.find_element(HomePage.individualTool[0], HomePage.individualTool[1].format(ID)+' h5').text
        toolPrice = self.driver.find_element(HomePage.individualTool[0], HomePage.individualTool[1].format(ID)+' span[data-test]').text
        self.driver.find_element(HomePage.individualTool[0], HomePage.individualTool[1].format(ID)).click()
        productPageObj = ProductPage(self.driver)
        return [productPageObj, toolName, toolPrice]