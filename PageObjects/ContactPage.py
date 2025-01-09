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

    # Function to populate the #first_name and #last_name input fields
    def populateNameElements(self, firstN, lastN):
        # Clearing the input fields prior to using the send_keys() actions
        self.driver.find_element(*ContactPage.firstName).clear()
        self.driver.find_element(*ContactPage.lastName).clear()
        self.driver.find_element(*ContactPage.firstName).send_keys(firstN)
        self.driver.find_element(*ContactPage.lastName).send_keys(lastN)

    # Function to populate the #email input field
    def populateEmailElement(self, emailID):
        # Clearing the input fields prior to using the send_keys() actions
        self.driver.find_element(*ContactPage.email).clear()
        self.driver.find_element(*ContactPage.email).send_keys(emailID)

    # Function to select the dropdown value according to index value of its option, value starts from 1 and not 0
    def selectDropDownValue(self, index):
        selectObj = Select(self.driver.find_element(*ContactPage.selectDropDown))
        selectObj.select_by_index(index)

    #Function to populate the #message textarea 
    def populateMessage(self, message):
        self.driver.find_element(*ContactPage.message).clear()
         # Clearing the textarea prior to using the send_keys() actions
        self.driver.find_element(*ContactPage.message).send_keys(message)

    # Function to click on the submitButton
    def clickSubmit(self):
        self.driver.find_element(*ContactPage.submitButton).click()

    # Function to get the successMessage
    def getSuccessMessageElement(self):
        # Using 'find_elements' so it returns an empty list if there is no such element
        return self.driver.find_elements(*ContactPage.successMessage)