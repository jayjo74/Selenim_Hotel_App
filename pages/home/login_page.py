from selenium.webdriver.common.by import By
# import logging
# import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver
from time import sleep

class login_page(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _userName_field = "username" #By.NAME
    _password_field = "password" #By.NAME
    _login_button = "login"  #By.NAME
    _loginFailed_msg = "//div[@class='auth_error']"

    # #Read each element  - don't need these step cause Action part already have this information
    # def getUserNameField(self):
    #     return self.driver.find_element(By.NAME, self._userName_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.NAME, self._password_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.NAME, self._login_button)

    #Action
    def enterUserName(self, username):
        self.sendKeys(username, self._userName_field, locatorType="name")
        self.log.info("Typed in user name filed - " + username)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="name")
        self.log.info("Typed in password filed - " + password)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")
        self.log.info("Clicked Login Button.")

    def login(self, username, password):
        self.enterUserName(username)
        sleep(1)
        self.enterPassword(password)
        sleep(1)
        self.clickLoginButton()

    #This step will be in the 'searchHotel_page'
    # def verifyLoginSuccessful(self):
    #     pass

    def verifyLoginFailed(self):
        result = self.isElementPresent(self._loginFailed_msg, locatorType= "xpath")
        return result




