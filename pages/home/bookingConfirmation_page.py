from selenium.webdriver.common.by import By
# import logging
# import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver
from time import sleep

class bookingConfirmation_page(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locator
    _searchHotelBtn = "search_hotel" # By.NAME
    _myLtineraryBtn = "my_itinerary" # By.NAME
    _logOutBtn = "logout" # By.NAME
    _orderNum = "order_no" # By.NAME

    # Actions
    def verifyBookConfirmationPage(self):
        self.waitForElement(locator=self._myLtineraryBtn, locatorType="name", timeout=30)
        result = self.isElementPresent(locator=self._orderNum, locatorType="name")
        return result

    def clickLogOutButton(self):
        self.elementClick(locator=self._logOutBtn, locatorType="name")
        self.log.info("Clicked Logout button.")
