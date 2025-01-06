import pytest, time
from Utilities.BaseClass import BaseClass
from PageObjects.CategoriesPage import Category

class TestCategoryPage(BaseClass):

    @pytest.mark.parametrize("categoryName", ['Hand Tools', 'Power Tools'])
    def test_HeadingText(self, categoryName):
        log = self.getLogger()
        categoryObj = Category(self.driver)
        self.verifyPageLoad(categoryObj.getToolContainerElement())
        heading = categoryObj.getHeading(categoryName)
        log.info(heading)
        assert categoryName in heading, 'Incorrect name within heading.'
    
    @pytest.mark.parametrize("categoryName", ['Power Tools', 'Hand Tools'])
    def test_ValidTools(self, categoryName):
        log = self.getLogger()
        categoryObj = Category(self.driver)
        if categoryName == "Hand Tools":
            categoryObj.selectHandTools()
            self.verifyPageLoad(categoryObj.getToolContainerElement())
            time.sleep(1)
            toolList = categoryObj.getToolList()
            toolNames = []
            for tool in toolList:
                tool = tool.text
                toolNames.append(tool)
                assert "hammer" in tool.lower() or "Saw" in tool or "Wrench" in tool or "Spanner" in tool or "Screwdriver" in tool or "Pliers" in tool or "Cutters" in tool, "The tool doesn't belong to Hammer/Saw/Wrench/Spanner/Screwdriver/Pliers/Cutters"
            log.info(toolNames)
        elif categoryName == "Power Tools":
            categoryObj.selectPowerTools()
            self.verifyPageLoad(categoryObj.getToolContainerElement())
            toolList = categoryObj.getToolList()
            toolNames = []
            for tool in toolList:
                tool = tool.text
                toolNames.append(tool)
                assert "Sander" in tool or "Saw" in tool or "Drill" in tool, "The tool doesn't belong to Sander/Saw/Drill"
            log.info(toolNames)


