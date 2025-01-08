from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class ContactPage:

    firstName = (By.ID, 'first_name')
    lastName = (By.ID, 'last_name')
    email = (By.ID, 'email')
    selectDropDown = (By.ID, 'subject')
    message = (By.ID, 'message')

    def __init__(self, driver):
        self.driver = driver

    def returnNameElements(self, firstN, lastN):
        self.driver.find_element(*ContactPage.firstName).send_keys(firstN)
        self.driver.find_element(*ContactPage.lastName).send_keys(lastN)

    def returnEmailElement(self, emailID):
        self.driver.find_element(*ContactPage.email).send_keys(emailID)

    def getSelectElement(self, text):
        selectObj = Select(self.driver.find_element(*ContactPage.selectDropDown))
        selectObj.select_by_visible_text(text)

    def getMessage(self, message):
        self.driver.find_element(*ContactPage.message).send_keys(message)