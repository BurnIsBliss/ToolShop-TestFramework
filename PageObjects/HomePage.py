from selenium.webdriver.common.by import By
from PageObjects.ProductPage import ProductPage
from Utilities.BaseClass import BaseClass
from PageObjects.ContactPage import ContactPage

class HomePage(BaseClass):

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

    # Function to return the 'tooList' variable
    def getToolContainerElement(self):
        return HomePage.toolList

    # Returns a list of all the tools in the page
    def getToolList(self):
        return self.driver.find_elements(*HomePage.toolList)
    
    # Returns the name of all the tools within the page as a list
    def getToolNames(self):
        return self.driver.find_elements(*HomePage.toolNames)
    
    # Returns the price of all the tools within the webpage as a list
    def getToolPrices(self):
        return self.driver.find_elements(*HomePage.toolPrices)

    # Returns the productPageObj, toolName and toolPrice as a list for a particular product 'ID'
    def getIndividualTool(self, ID):
        toolName = self.driver.find_element(HomePage.individualTool[0], HomePage.individualTool[1].format(ID)+' h5').text
        toolPrice = self.driver.find_element(HomePage.individualTool[0], HomePage.individualTool[1].format(ID)+' span[data-test]').text
        self.driver.find_element(HomePage.individualTool[0], HomePage.individualTool[1].format(ID)).click()
        productPageObj = ProductPage(self.driver)
        return [productPageObj, toolName, toolPrice]
    
    # Function to click of the 'Hand Tools' category
    def selectHandTools(self):
        self.driver.find_element(*HomePage.categoryDropDown).click()
        self.driver.find_element(*HomePage.handToolsLink).click()
    
    # Function to click of the 'Power Tools' category
    def selectPowerTools(self):
        self.driver.find_element(*HomePage.categoryDropDown).click()
        self.driver.find_element(*HomePage.powerToolsLink).click()

    # Function to open the 'Contact' page
    def navigateContactPage(self):
        self.driver.find_element(*HomePage.contactButton).click()
        contactPageObj = ContactPage(self.driver)
        return contactPageObj