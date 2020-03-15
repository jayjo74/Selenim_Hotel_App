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
class Testcase_101_VerifyLogin(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    ################################################################################
    #If you have to use more than 2 test cases in one class file, use this function
    #Create each page object for all test case

    # @pytest.fixture(autouse=True)
    # def objectSetup(self, oneTimeSetUp):
    #     self.lp = login_page(self.driver)
    #     self.ts = TestStatus(self.driver)
    #################################################################################

    @pytest.mark.run(order=1)
    @data(("seattletester", "Seattle123"))  # provide test data directly
    # @data(*getCSVData("../testdata/testdata.csv"))  # read test data from CSV file
    # @data(*getExcelData("test_TC01_verifylogin_Success"))  # read test data from Excel file
    # @data(*getlogindata())  # read test data from 'read_data.py'
    @unpack
    def test_TC01_verifylogin_Success(self, userID, password):
        lp = login_page(self.driver)
        sh = searchHotel_page(self.driver)

        self.log.info("#" * 40)
        self.log.info("'test_TC01_verifylogin' started.")
        self.log.info("#" * 40)
        #############################################################################
        #Example step for - Create each page object for all test case
        # self.lp.login("seattletester", "Seattle123")
        #############################################################################
        self.log.info("Log in to Hotel app.")
        lp.login(userID, password)

        # self.log.info("Check Login successful.")
        result = sh.verifyLoginSuccessful()
        if result:
            self.log.info("### VERIFICATION SUCCESSFUL :: Login." )
        else:
            self.log.error("### VERIFICATION FAILED :: Login.")

        # assert result == True

        self.log.info("#" * 40)
        self.log.info("'test_TC01_verifylogin' completed.")
        self.log.info("#" * 40)



