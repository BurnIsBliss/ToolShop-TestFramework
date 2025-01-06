from selenium.webdriver.common.by import By
from PageObjects.ProductPage import ProductPage

class HomePage:
    toolList = (By.CSS_SELECTOR, '.container > .card')
    toolNames = (By.CSS_SELECTOR, '.card-title')
    toolPrices = (By.XPATH, "//span[@data-test='product-price']")
    individualTool = (By.CSS_SELECTOR, "a[data-test='product-{}']")
    homeButton = (By.PARTIAL_LINK_TEXT, 'Home')
    categoryDropDown = (By.PARTIAL_LINK_TEXT, 'Categories')
    handToolsLink = (By.PARTIAL_LINK_TEXT, 'Hand Tools')
    powerToolsLink = (By.PARTIAL_LINK_TEXT, 'Power Tools')
    contactButton = (By.PARTIAL_LINK_TEXT, 'Contact')


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
    
    def selectHandTools(self):
        self.driver.find_element(*HomePage.categoryDropDown).click()
        self.driver.find_element(*HomePage.handToolsLink).click()
    
    def selectPowerTools(self):
        self.driver.find_element(*HomePage.categoryDropDown).click()
        self.driver.find_element(*HomePage.powerToolsLink).click()