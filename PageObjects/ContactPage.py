from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class ContactPage:

    firstName = (By.ID, 'first_name')
    lastName = (By.ID, 'last_name')
    email = (By.ID, 'email')
    selectDropDown = (By.ID, 'subject')
    message = (By.ID, 'message')
    submitButton = (By.CSS_SELECTOR, 'input.btnSubmit')
    successMessage = (By.CSS_SELECTOR, '.alert-success')

    def __init__(self, driver):
        self.driver = driver

    def populateNameElements(self, firstN, lastN):
        self.driver.find_element(*ContactPage.firstName).clear()
        self.driver.find_element(*ContactPage.lastName).clear()
        self.driver.find_element(*ContactPage.firstName).send_keys(firstN)
        self.driver.find_element(*ContactPage.lastName).send_keys(lastN)

    def populateEmailElement(self, emailID):
        self.driver.find_element(*ContactPage.email).clear()
        self.driver.find_element(*ContactPage.email).send_keys(emailID)

    def selectDropDownValue(self, index):
        selectObj = Select(self.driver.find_element(*ContactPage.selectDropDown))
        selectObj.select_by_index(index)

    def populateMessage(self, message):
        self.driver.find_element(*ContactPage.message).clear()
        self.driver.find_element(*ContactPage.message).send_keys(message)

    def clickSubmit(self):
        self.driver.find_element(*ContactPage.submitButton).click()

    def getSuccessMessageElement(self):
        # Using 'find_elements' so it returns an empty list if there is no such element
        return self.driver.find_elements(*ContactPage.successMessage)