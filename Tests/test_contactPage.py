import pytest

from Utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage
from TestData.ContactPageTestData import ContactPageData

class TestContactPage(BaseClass):

    @pytest.mark.parametrize('first, last', ContactPageData.nameData)
    def test_NameField(self, first, last):
        log = self.getLogger()
        homePageObj = HomePage(self.driver)
        contactPageObj = homePageObj.navigateContactPage()
        contactPageObj.populateNameElements(first, last)
        contactPageObj.populateEmailElement('a@a.aa')
        contactPageObj.selectDropDownValue(1)
        contactPageObj.populateMessage('abcdefghijklmnopqrstuvwxyz_abcdefghijklmnopqrstuvwxyz')
        contactPageObj.clickSubmit()
        successMessage = contactPageObj.getSuccessMessageElement()
        log.debug('firstName: {}, lastName: {}'.format(first, last))
        assert len(successMessage) > 0, 'The test for the values: {} {} FAILED'.format(first, last)
        self.driver.refresh()

    @pytest.mark.parametrize('email', ContactPageData.emailData)
    def test_EmailCheck(self, email):
        log = self.getLogger()
        homePageObj = HomePage(self.driver)
        contactPageObj = homePageObj.navigateContactPage()
        contactPageObj.populateNameElements('First Name', 'Last Name')
        contactPageObj.populateEmailElement(email)
        contactPageObj.selectDropDownValue(1)
        contactPageObj.populateMessage('abcdefghijklmnopqrstuvwxyz_abcdefghijklmnopqrstuvwxyz')
        contactPageObj.clickSubmit()
        successMessage = contactPageObj.getSuccessMessageElement()
        log.info('Email ID: {}'.format(email))
        assert len(successMessage) > 0, 'The test with the value: {} FAILED'.format(email)
        self.driver.refresh()

    @pytest.mark.parametrize('index', ContactPageData.dropdownData)
    def test_Dropdown(self, index):
        log = self.getLogger()
        homePageObj = HomePage(self.driver)
        contactPageObj = homePageObj.navigateContactPage()
        contactPageObj.populateNameElements('First Name', 'Last Name')
        contactPageObj.populateEmailElement('email@m.mm')
        contactPageObj.selectDropDownValue(index)
        contactPageObj.populateMessage('abcdefghijklmnopqrstuvwxyz_abcdefghijklmnopqrstuvwxyz')
        contactPageObj.clickSubmit()
        successMessage = contactPageObj.getSuccessMessageElement()
        log.info('Index Value: {}'.format(index))
        assert len(successMessage) > 0, 'The test with the value: {} FAILED!!!'.format(index)
        self.driver.refresh()
    
    @pytest.mark.parametrize('message', ContactPageData.messageData)
    def test_MessageField(self, message):
        log = self.getLogger()
        homePageObj = HomePage(self.driver)
        contactPageObj = homePageObj.navigateContactPage()
        contactPageObj.populateNameElements('First Name', 'Last Name')
        contactPageObj.populateEmailElement('email@m.mm')
        contactPageObj.selectDropDownValue(1)
        contactPageObj.populateMessage(message)
        contactPageObj.clickSubmit()
        successMessage = contactPageObj.getSuccessMessageElement()
        log.info('Message: {}'.format(message))
        assert len(successMessage) > 0, 'The test with the value: {} FAILED!!!'.format(message)
        self.driver.refresh()