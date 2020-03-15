import logging
from time import sleep
import utilities.custom_logger as cl
import unittest
import pytest

from pages.home.bookHotel_page import bookHotel_page
from pages.home.bookingConfirmation_page import bookingConfirmation_page
from pages.home.login_page import login_page
from pages.home.logout_page import logout_page
from pages.home.searchHotel_page import searchHotel_page
from pages.home.selectHotel_page import selectHotel_page
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from utilities.read_data import getExcelData
from utilities.read_data import getlogindata

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class Testcase_109_VerifyLogout(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    @pytest.mark.run(order=1)
    @data(("seattletester", "Seattle123"))  # provide test data directly
    # @data(*getCSVData("../testdata/testdata.csv"))  # read test data from CSV file
    # @data(*getExcelData("test_TC01_verifylogin_Success"))  # read test data from Excel file
    # @data(*getlogindata())  # read test data from 'read_data.py'
    @unpack
    def test_TC09_verifyLogout(self, userID, password):
        lp = login_page(self.driver)
        sh = searchHotel_page(self.driver)
        sl = selectHotel_page(self.driver)
        bh = bookHotel_page(self.driver)
        bc = bookingConfirmation_page(self.driver)
        lo = logout_page(self.driver)

        self.log.info("#" * 40)
        self.log.info("'test_TC09_verifyLogout' started.")
        self.log.info("#" * 40)

        self.log.info("Log in to Hotel app.")
        lp.login(userID, password)
        result = sh.verifyLoginSuccessful()
        assert result == True, "### VERIFICATION FAILED :: Login."
        sleep(1)

        self.log.info("Input data in Search Hotel Page.")
        sh.inputSearchPageData("Sydney", "Hotel Creek", "Standard", "1 - One", "12/10/2020", "12/15/2020", "1 - One",
                               "1 - One")
        sleep(1)

        self.log.info("Click Search button.")
        sh.clickSearchButton()

        self.log.info("Search Page verify.")
        result = sl.verifySelectPage()
        assert result == True, "### VERIFICATION FAILED :: Select Page."
        sleep(1)

        sl.clickRadioButton01()
        sleep(1)

        sl.clickContinueButton()
        result = bh.verifyBookHotelPage()
        assert result == True, "### VERIFICATION FAILED :: Book Hotel Page."
        sleep(1)

        bh.inputBookHotelData("Jay", "Jo", "Bellevue", "1234567898765432", "VISA", "May", "2021", "123")
        sleep(1)

        bh.clickBookNowButton()
        result = bc.verifyBookConfirmationPage()
        assert result == True, "### VERIFICATION FAILED :: Book Confirmation Page."
        sleep(1)

        bc.clickLogOutButton()
        lo.verifyLogoutPage()

        self.log.info("#" * 40)
        self.log.info("'test_TC09_verifyLogout' completed.")
        self.log.info("#" * 40)