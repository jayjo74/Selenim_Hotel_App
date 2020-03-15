from selenium.webdriver.common.by import By
# import logging
# import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver
from time import sleep

class selectHotel_page(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locator
    _hotelName01 = "hotel_name_0" # By.NAME
    _selectRadioBtn01 = "radiobutton_0" # By.NAME
    _continueBtn = "continue" # By.NAME
    _selectHotelTitle = "login_title" #By.CLASS_NAME

    #Actions
    def verifySelectPage(self):
        self.waitForElement(locator=self._selectHotelTitle, locatorType="class", timeout=20)
        result = self.isElementPresent(locator=self._continueBtn, locatorType="name")
        return result

    def clickRadioButton01(self):
        self.elementClick(self._selectRadioBtn01, locatorType="name")
        self.log.info("Selected first row in Select Hotel Page.")

    def clickContinueButton(self):
        self.elementClick(self._continueBtn, locatorType="name")
        self.log.info("Clicked 'Continue' button.")

    def verifyHotelNameRow01(self):
        result = self.getAttributeValue(locator=self._hotelName01, locatorType="name", attribute="value")
        return result



