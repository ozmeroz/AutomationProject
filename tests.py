from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import unittest
from Pages.mainPage import MainPage
class MyTestCase(unittest.TestCase):



    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='c:/seleniumDriver/chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.advantageonlineshopping.com/")
        self.driver.maximize_window()
        self.mainPage = MainPage(self.driver)
        self.login()

    def tearDown(self):
        self.driver.close()

    def login(self):
        self.mainPage.usermenu().click()
        self.mainPage.usernameField()
        self.mainPage.passwordField()
        self.mainPage.signInBtn().click()
        self.assertTrue(self.mainPage.loggedUserName()=='tomoz')


