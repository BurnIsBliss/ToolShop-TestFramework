from selenium.webdriver.common.by import By
from Utilities.BaseClass import BaseClass

class ProductPage(BaseClass):

    productName = (By.XPATH, "//h1[@data-test='product-name']")
    productPrice = (By.CSS_SELECTOR, 'span[data-test="unit-price"]')
    categoryTag = (By.XPATH, "//span[@aria-label='category']")
    brandName = (By.XPATH, '//span[@aria-label="brand"]')
    relatedProducts = (By.CSS_SELECTOR, ".col > .container > a h5")

    def __init__(self, driver):
        self.driver = driver

    # Function to return the name of the product in the Product Page
    def getProductName(self):
        self.verifyPageLoad(ProductPage.productName)
        return self.driver.find_element(*ProductPage.productName).text
    
    # Function to return the price of the product in the Product Page
    def getProductPrice(self):
        self.verifyPageLoad(ProductPage.productPrice)
        return self.driver.find_element(*ProductPage.productPrice).text
    
    # Function to return the category of the product in the Product Page
    def getCategoryTag(self):
        self.verifyPageLoad(ProductPage.categoryTag)
        return self.driver.find_element(*ProductPage.categoryTag).text
    
    # Function to return the brand of the product in the Product Page
    def getBrandName(self):
        self.verifyPageLoad(ProductPage.brandName)
        return self.driver.find_element(*ProductPage.brandName).text
    
    # Function to return the Related Products (if any) of the particular product in the Product Page
    def getRelatedProductsList(self):
        return self.driver.find_elements(*ProductPage.relatedProducts)
