import unittest
from tests.test_TC101_VerityLogIn import Testcase_101_VerifyLogin
from tests.test_TC102_VerifyCheckOutError import Testcase_102_VerifyCheckOutError

#Get all tests from the test classed
tc1 = unittest.TestLoader().loadTestsFromTestCase(Testcase_101_VerifyLogin)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Testcase_102_VerifyCheckOutError)

#Create a test suite combinin all test clases
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)

