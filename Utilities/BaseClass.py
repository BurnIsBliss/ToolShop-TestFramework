import pytest
import logging, inspect

@pytest.mark.usefixtures('SetUp')
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('./Logs/logFile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

