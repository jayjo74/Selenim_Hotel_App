import logging
from time import sleep
import utilities.custom_logger as cl
import unittest
import pytest
from pages.home.login_page import login_page
from pages.home.searchHotel_page import searchHotel_page
from pages.home.selectHotel_page import selectHotel_page
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from utilities.read_data import getExcelData
from utilities.read_data import getlogindata

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class Testcase_104_VerifyLocation(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    @pytest.mark.run(order=1)
    @data(("seattletester", "Seattle123"))  # provide test data directly
    # @data(*getCSVData("../testdata/testdata.csv"))  # read test data from CSV file
    # @data(*getExcelData("test_TC01_verifylogin_Success"))  # read test data from Excel file
    # @data(*getlogindata())  # read test data from 'read_data.py'
    @unpack
    def test_TC04_verifyLocation(self, userID, password):
        lp = login_page(self.driver)
        sh = searchHotel_page(self.driver)
        sl = selectHotel_page(self.driver)

        self.log.info("#" * 40)
        self.log.info("'test_TC04_verifyLocation' started.")
        self.log.info("#" * 40)

        self.log.info("Log in to Hotel app.")
        lp.login(userID, password)
        result = sh.verifyLoginSuccessful()
        if result:
            self.log.info("### VERIFICATION SUCCESSFUL :: Login.")
        else:
            self.log.error("### VERIFICATION FAILED :: Login.")
        sleep(1)

        self.log.info("Input data in Search Hotel Page.")
        sh.inputSearchPageData("Sydney", "Hotel Creek", "Standard", "1 - One", "12/10/2020", "12/15/2020", "1 - One",
                               "1 - One")
        sleep(1)

        self.log.info("Click Search button.")
        sh.clickSearchButton()

        result = sl.verifySelectPage()
        assert result == True, "### VERIFICATION FAILED :: Select Page."
        sleep(1)

        result = sl.verifyHotelNameRow01()
        assert result == "Hotel Creek", "### VERIFICATION FAILED :: Verify Hotel name - Hotel Creek."

        self.log.info("'test_TC04_verifyLocation' completed.")
        self.log.info("#" * 40)
        self.log.info("#" * 40)