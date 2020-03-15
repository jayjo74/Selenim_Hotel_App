import logging
from time import sleep
import utilities.custom_logger as cl
import unittest
import pytest
from pages.home.login_page import login_page
from pages.home.searchHotel_page import searchHotel_page
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from utilities.read_data import getExcelData
from utilities.read_data import getlogindata

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class Testcase_102_VerifyCheckOutError(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    @pytest.mark.run(order=1)
    @data(("seattletester", "Seattle123"))  # provide test data directly
    # @data(*getCSVData("../testdata/testdata.csv"))  # read test data from CSV file
    # @data(*getExcelData("test_TC01_verifylogin_Success"))  # read test data from Excel file
    # @data(*getlogindata())  # read test data from 'read_data.py'
    @unpack
    def test_TC02_verifyCheckoutError(self, userID, password):
        lp = login_page(self.driver)
        sh = searchHotel_page(self.driver)

        self.log.info("#" * 40)
        self.log.info("'test_TC02_verifyCheckoutError' started.")
        self.log.info("#" * 40)

        self.log.info("Log in to Hotel app.")
        lp.login(userID, password)

        result = sh.verifyLoginSuccessful()
        if result:
            self.log.info("### VERIFICATION SUCCESSFUL :: Login." )
        else:
            self.log.error("### VERIFICATION FAILED :: Login.")
        sleep(1)

        self.log.info("Input data in Search Hotel Page.")
        sh.inputSearchPageData("Sydney", "Hotel Creek", "Standard", "1 - One", "12/20/2020", "12/15/2020", "1 - One", "1 - One")
        sleep(1)

        self.log.info("Click Search button.")
        sh.clickSearchButton()
        sleep(1)

        result = sh.verifyCheckInDateFailed()
        if result:
            self.log.info("### VERIFICATION SUCCESSFUL :: Check in date error message." )
        else:
            self.log.error("### VERIFICATION FAILED :: Check in date error message.")

        self.log.info("#" * 40)
        self.log.info("'test_TC02_verifyCheckoutError' completed.")
        self.log.info("#" * 40)



