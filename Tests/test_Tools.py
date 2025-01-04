import pytest

from Utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage

class TestingTools(BaseClass):

    def test_TotalNumberOfTools(self):
        log = self.getLogger()
        homeObj = HomePage(self.driver)
        self.verifyPageLoad(homeObj.getToolContainerElement()[1])
        totalTools = homeObj.getToolList()
        log.info("Total number of tools: {}".format(len(totalTools)))
        assert len(totalTools) == 26, 'The total number of tools should be 26.'
    
    def test_Capitalization(self):
        log = self.getLogger()
        homeObj = HomePage(self.driver)
        self.verifyPageLoad(homeObj.getToolContainerElement()[1])
        names = homeObj.getToolNames()
        for tool in names:
            toolNameSplit = (tool.text).split(' ')
            for individualName in toolNameSplit:
                if individualName[0].isnumeric() or individualName == 'with' or individualName[0] == '(':
                    log.debug("Skipped words {}".format(individualName))
                    continue
                assert individualName[0].isupper(), 'Issue with Grammar in tool naming.'

    def test_PriceFormat(self):
        log = self.getLogger()
        homeObj = HomePage(self.driver)
        self.verifyPageLoad(homeObj.getToolContainerElement()[1])
        prices = homeObj.getToolPrices()
        for price in prices:
            log.info(price.text)
            assert '$' in price.text, 'Wrong currency format mentioned for the tools.'
            

    




