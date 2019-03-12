"""
Qxf2: Example script to run one test against ATP_WTA app using Appium
The test will navigate to ATP Singles Rankings list and confirm that Novak
Djokovic is the top player listed and get his personal details from a table.
 
""" 
 
import unittest, time, os 
from appium import webdriver 
from time import sleep
 
class Android_ATP_WTA(unittest.TestCase):
    "Class to run tests against the ATP WTA app"
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'emulator-5554'
        # Since the app is already installed launching it using package and activity name
        desired_caps['appPackage'] = 'com.android.calculator2'
        desired_caps['appActivity'] = 'com.android.calculator2.Calculator'
        # Adding appWait Activity since the activity name changes as the focus shifts to the ATP WTA app's first page
        #desired_caps['appWaitActivity'] = '.activity.root.TournamentList'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
 
    def tearDown(self):
        "Tear down the test"
        self.driver.quit()
 
    def test_atp_wta(self):
        "Testing the ATP WTA app "
        self.driver.implicitly_wait(30)
        time.sleep(5)
 
        # click on the nuber 8 - locate via ID
        number_8 = self.driver.find_element_by_id('com.android.calculator2:id/digit_8')
        number_8.click()
 
        # click on '+' operator - locate via uiautomator text
        operator = self.driver.find_element_by_android_uiautomator('new UiSelector().text("+")')
        operator.click()
 
        # click on the number 8 - locate via uiautomator index number 
        number_2 = self.driver.find_element_by_android_uiautomator('new UiSelector().index(7)')
        number_2.click()

        
        # click on the operator '=' - locate via ID 
        operator_eq = self.driver.find_element_by_id('com.android.calculator2:id/eq')
        operator_eq.click()
 
        # Assert that the result is equal to 10
        elmnt = self.driver.find_element_by_id('com.android.calculator2:id/result')
        self.assertEqual('10', elmnt.get_attribute('text'))
        print elmnt.get_attribute('text')
 
        elmnt = self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index=0]")
        elmnt.click()
        
        '''
        # EXAMPLE - loop through table elements
        # Print the contents of Table listed for the top ranked player
        table = self.driver.find_element_by_android_uiautomator("new UiSelector().className(android.widget.TableLayout)")
        rows = table.find_elements_by_class_name('android.widget.TableRow')
        for i in range(0, len(rows)):
            cols = rows[i].find_elements_by_class_name('android.widget.TextView')
            for j in range(0, len(cols)):
                print(cols[j].get_attribute('text')+" -- "),
            print("")
        '''
 
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Android_ATP_WTA)
    unittest.TextTestRunner(verbosity=2).run(suite)
