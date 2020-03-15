from selenium.webdriver.common.by import By
# import logging
# import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver
from time import sleep

class logout_page(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _logoutmessage = "//td[@class='reg_success']" #By.XPATH

    #Action
    def verifyLogoutPage(self):
        self.waitForElement(locator=self._logoutmessage, locatorType="xpath", timeout=30)
        result = self.getText(locator=self._logoutmessage, locatorType="xpath")
        assert result == "You have successfully logged out. Click here to login again", "### VERIFICATION FAILED :: Logout Page."
