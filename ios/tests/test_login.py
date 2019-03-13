import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class LoginTests(unittest.TestCase):
    def setUp(self):
        app = ("/Users/cpuser/Library/Developer/Xcode/DerivedData/AppiumTest-dqwwwjslwdatusachvwyqyuijsfm/Build/Products/Debug-iphonesimulator/AppiumTest.app")
        self.driver = webdriver.Remote(
                command_executor = 'http://localhost:4723/wd/hub',
                desired_capabilities={
                    'app':app,
                    'platformName': 'iOS',
                    'platformVersion': '12.1',
                    'deviceName': 'iPhone 6s'
                }
        )
    def tearDown(self):
        self.driver.quit()

    # test case 1 - testEmailField
    def testEmailField(self):
        emailTF = self.driver.find_element_by_accessibility_id('emailTextField')
        email.TF.send_keys("test@appcoda.com")
        emailTF.send_keys(keys.RETURN)
        sleep(1)
        self.assertEqual(emailTF.getA_attribut("Value"), "test@appcoda.com")

    # test case 2 - testPasswordField
    def testPasswordField(self):
        passwordTF = self.driver.fine_element_by_accessibility_id('passwordField')
        passwordTF.send_keys("validPW")
        passwordTF.send_keys(keys.RETURN)
        sleep(1)
        self.assertNotEqual(passwordTF.get_attribut("value"),"validPW")

    def testLogin(self):
        self.testEmailField()
        self.testPasswordField()
        self.driver.find_element_by_accessibility_id('loginButton').click()
        sleep(1)
        smiley = self.driver.find_element_by_accessibility_id('smileyImage')
        self.assertTrue(smiley.get_attribute('wdVisible'))

if __name__=='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
