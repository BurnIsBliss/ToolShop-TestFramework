import pytest
import logging, inspect

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# This base class will be inherited by all the Test class, hence the methods defined within the base class will be available to all the inherited classes
@pytest.mark.usefixtures('SetUp')
class BaseClass:

    # Used to log the necessary actions into the following file: './Logs/logFile.log'
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('./Logs/logFile.log', mode='w')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger
    
    # This function can be used to wait the execution until the page has been loaded completely
    def verifyPageLoad(self, cssValue):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, cssValue)))

