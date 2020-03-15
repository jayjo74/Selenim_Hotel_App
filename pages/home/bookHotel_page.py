from selenium.webdriver.common.by import By
# import logging
# import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver
from time import sleep

class bookHotel_page(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locator
    _firstNameTxt = "first_name"  # By.NAME
    _lastNameTxt = "last_name" # By.NAME
    _billingAddressTxt = "address" # By.NAME
    _creditcardNumTxt = "cc_num" # By.NAME
    _creditcardTypeSel = "cc_type" # By.NAME
    _creditcardExpiryMonthSel = "cc_exp_month" # By.NAME
    _creditcardExpiryYearSel = "cc_exp_year" # By.NAME
    _creditcardCCVTxt = "cc_cvv" # By.NAME
    _booknowBtn = "book_now" # By.NAME

    # Actions
    def verifyBookHotelPage(self):
        self.waitForElement(locator=self._booknowBtn, locatorType="name", timeout=30)
        result = self.isElementPresent(locator=self._firstNameTxt, locatorType="name")
        return result

    def enterFirstName(self, firstname):
        self.sendKeys(firstname, self._firstNameTxt, locatorType="name")
        self.log.info("Typed in First Name filed - " + firstname)

    def enterLastName(self, lastname):
        self.sendKeys(lastname, self._lastNameTxt, locatorType="name")
        self.log.info("Typed in Last Name filed - " + lastname)

    def enterBillingAddress(self, address):
        self.sendKeys(address, self._billingAddressTxt, locatorType="name")
        self.log.info("Typed in Billing Address filed - " + address)

    def enterCreditCardNumber(self, ccnum):
        self.sendKeys(ccnum, self._creditcardNumTxt, locatorType="name")
        self.log.info("Typed in Credit Card Number filed - " + ccnum)

    def selectCreditCardType(self, ccard):
        self.selectByText(locator=self._creditcardTypeSel, locatorType="name", visibletext=ccard)
        self.log.info("Selected in Credit Card Type - " + ccard)

    def selectCreditCardMonth(self, ccardMon):
        self.selectByText(locator=self._creditcardExpiryMonthSel, locatorType="name", visibletext=ccardMon)
        self.log.info("Selected in Credit Card Expiry Month - " + ccardMon)

    def selectCreditCardYear(self, ccardYear):
        self.selectByText(locator=self._creditcardExpiryYearSel, locatorType="name", visibletext=ccardYear)
        self.log.info("Selected in Credit Card Expiry Year - " + ccardYear)

    def enterCreditCardCVV(self, cvv):
        self.sendKeys(cvv, self._creditcardCCVTxt, locatorType="name")
        self.log.info("Typed in Billing Address filed - " + cvv)

    def clickBookNowButton(self):
        self.elementClick(locator=self._booknowBtn, locatorType="name")
        self.log.info("Clicked Book Now button.")

    def inputBookHotelData(self, firstname, lastname, address, ccnum, ccard, ccardMon, ccardYear, cvv):
        self.enterFirstName(firstname)
        sleep(1)
        self.enterLastName(lastname)
        sleep(1)
        self.enterBillingAddress(address)
        sleep(1)
        self.enterCreditCardNumber(ccnum)
        sleep(1)
        self.selectCreditCardType(ccard)
        sleep(1)
        self.selectCreditCardMonth(ccardMon)
        sleep(1)
        self.selectCreditCardYear(ccardYear)
        sleep(1)
        self.enterCreditCardCVV(cvv)

