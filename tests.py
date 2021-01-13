from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import unittest
from Pages import mainPage
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='c:/seleniumDriver/chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.advantageonlineshopping.com/")
        self.driver.maximize_window()
        self.login()


    def login(self):
        mainPage.usermenu().click()
        mainPage.usernameField()
        mainPage.passwordField()
        mainPage.signInBtn().click()


