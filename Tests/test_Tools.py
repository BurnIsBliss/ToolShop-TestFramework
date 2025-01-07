from Utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage

class TestingTools(BaseClass):

    def test_TotalNumberOfTools(self):
        log = self.getLogger()
        homeObj = HomePage(self.driver)
        self.verifyPageLoad(homeObj.getToolContainerElement())
        totalTools = homeObj.getToolList()
        log.info("Total number of tools: {}".format(len(totalTools)))
        assert len(totalTools) == 26, 'The total number of tools should be 26.'
    
    def test_Capitalization(self):
        log = self.getLogger()
        homeObj = HomePage(self.driver)
        self.verifyPageLoad(homeObj.getToolContainerElement())
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
        self.verifyPageLoad(homeObj.getToolContainerElement())
        prices = homeObj.getToolPrices()
        priceList = []
        for price in prices:
            priceList.append(price.text)
            assert '$' in price.text, 'Wrong currency format mentioned for the tools.'
        log.info(priceList)
            
    def test_ToolDetails(self):
        log = self.getLogger()
        homeObj = HomePage(self.driver)
        self.verifyPageLoad(homeObj.getToolContainerElement())
        for i in range(1, 27):
            toolDetails = homeObj.getIndividualTool(str(i))
            log.info(toolDetails[0].getProductName() + ' ' + toolDetails[0].getProductPrice()) 
            assert toolDetails[0].getProductName() == toolDetails[1] and toolDetails[0].getProductPrice() in toolDetails[2], 'The name of the Tool or the Price of the tool is incorrect'
            self.driver.back()
            self.verifyPageLoad(homeObj.getToolContainerElement())

    def test_BrandNameCheck(self):
        log = self.getLogger()
        homeObj = HomePage(self.driver)
        self.verifyPageLoad(homeObj.getToolContainerElement())
        for i in range(1, 27):
            toolDetails = homeObj.getIndividualTool(str(i))
            brandName = toolDetails[0].getBrandName()
            log.info(brandName)
            assert 'Brand name 1' in brandName or 'Brand name 2' in brandName, 'Incorrect brand name for the tools'
            self.driver.back()
            self.verifyPageLoad(homeObj.getToolContainerElement())

    




