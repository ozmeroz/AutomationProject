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
        self.main = MainPage(self.driver)
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)


    def tearDown(self):
       self.main.endtest()


    def test_ex1(self):
        # self.main.usermenu().click() #login
        # self.main.usernameField() #login
        # self.main.passwordField() #login
        # self.main.signInBtn().click() #login
        self.main.tablets().click() #enter tablets category
        self.main.tablets_elitepad() #enter specific product
        self.main.plus().click() #add quantity
        self.main.add_to_cart().click() #add to cart
        self.main.tablets_HPelite() #enter specific product
        self.main.plus().click() #add quantity
        self.main.plus().click() #add quantity
        self.main.add_to_cart().click() #add to cart
        self.main.hoverCart() #hover over cart button to open cart summary
        self.assertIn("5", self.main.checkTotalItems())

    def test_ex2(self):
        self.main.tablets().click()  # enter tablets category
        self.main.tablets_elitepad()  # enter specific product
        self.main.plus().click()  # add quantity
        self.main.add_to_cart().click()  # add to cart
        self.main.tablets_HPelite()  # enter specific product
        self.main.plus().click()  # add quantity
        self.main.plus().click()  # add quantity
        self.main.add_to_cart().click()  # add to cart
        self.main.tablets_HP_PRO()
        self.main.plus().click()  # add quantity
        self.main.plus().click()  # add quantity
        self.main.plus().click()  # add quantity
        self.main.add_to_cart().click()  # add to cart
        text1 = print(self.main.miniCartTable(2, 1).text)
        price1 = print(self.main.miniCartTable(2, 2).text)
        text2=print(self.main.miniCartTable(1,1).text)
        price2=print(self.main.miniCartTable(1, 2).text)
        # self.main.hoverCart()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//tool-tip-cart/div/table/tbody/tr[1]/td[3]")))
        text3 = print(self.main.miniCartTable(0, 1).text)
        self.main.hoverCart()
        price3 = print(self.main.miniCartTable(0, 2).text)








