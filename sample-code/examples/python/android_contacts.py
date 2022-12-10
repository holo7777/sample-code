import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
from selenium.webdriver.common.by import By

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['app'] = PATH(
            '../../../sample-code/apps/ContactManager/ContactManager.apk'
        )
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = '.ContactManager'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self):
        self.driver.implicitly_wait(3)
        # el = self.driver.find_element_by_accessibility_id("Add Contact")
        # el = self.driver.find_element(By.ID, "Add Contact")
        el = self.driver.find_element(By.ID, "com.example.android.contactmanager:id/addContactButton")
        el.click()

        # textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields = self.driver.find_elements(By.CLASS_NAME, "android.widget.EditText")
        textfields[0].send_keys("Appium User")
        textfields[2].send_keys("someone@appium.io")

        self.assertEqual('Appium User', textfields[0].text)
        self.assertEqual('someone@appium.io', textfields[2].text)

        # self.driver.find_element_by_accessibility_id("Save").click()
        self.driver.find_element(By.ID, "com.example.android.contactmanager:id/contactSaveButton").click()

        # for some reason "save" breaks things
        # alert = self.driver.switch_to.alert.dismiss()
        # alert = self.driver.sw

        # no way to handle alerts in Android
        # self.driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()

        self.driver.press_keycode(3)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
