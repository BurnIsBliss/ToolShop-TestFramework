from selenium.webdriver.common.by import By

class ProductPage:

    productName = (By.XPATH, "//h1[@data-test='product-name']")
    productPrice = (By.CSS_SELECTOR, 'span[data-test="unit-price"]')
    categoryTag = (By.XPATH, "//span[@aria-label='category']")
    relatedProducts = (By.CSS_SELECTOR, ".col > .container > a h5")

    def __init__(self, driver):
        self.driver = driver

    def getProductName(self):
        return self.driver.find_element(*ProductPage.productName).text
    
    def getProductPrice(self):
        return self.driver.find_element(*ProductPage.productPrice).text
    
    def getCategoryTag(self):
        return self.driver.find_element(*ProductPage.categoryTag)
    
    def getRelatedProductsList(self):
        return self.driver.find_elements(*ProductPage.relatedProducts)




