import pytest, time

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
        contactPageObj.selectDropDownValue(0)
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
        assert len(successMessage) > 0, 'The test with for the value: {}'.format(email)
        self.driver.refresh()

