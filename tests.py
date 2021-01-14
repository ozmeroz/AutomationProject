from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import unittest
from Pages.categoryPage import CategoryPage
from Pages.mainPage import MainPage
from Pages.productPage import ProductPage
from Pages.tablets import Tablets
class MyTestCase(unittest.TestCase):



    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='c:/seleniumDriver/chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.advantageonlineshopping.com/")
        self.driver.maximize_window()
        self.main = MainPage(self.driver)
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)
        self.category=CategoryPage(self.driver)
        self.product=ProductPage(self.driver)
        self.tablets=Tablets(self.driver)


    def tearDown(self):
       self.main.endtest()


    def test_ex1(self):
        # self.main.usermenu().click() #login
        # self.main.usernameField() #login
        # self.main.passwordField() #login
        # self.main.signInBtn().click() #login
        self.category.tablets_category().click() #enter tablets category
        self.tablets.tablets_elitepad() #enter specific product
        self.product.plus().click() #add quantity
        self.product.add_to_cart().click() #add to cart
        self.tablets.tablets_HPelite() #enter specific product
        self.product.plus().click() #add quantity
        self.product.plus().click() #add quantity
        self.product.add_to_cart().click() #add to cart
        self.main.hoverCart() #hover over cart button to open cart summary
        self.assertIn("5", self.main.checkTotalItems())

    def test_ex2(self):
        self.category.tablets_category().click()  # enter tablets category
        self.tablets.tablets_elitepad()  # enter specific product
        self.product.plus().click()  # add quantity
        self.product.add_to_cart().click()  # add to cart
        self.tablets.tablets_HPelite()  # enter specific product
        self.product.plus().click()  # add quantity
        self.product.plus().click()  # add quantity
        self.product.add_to_cart().click()  # add to cart
        self.tablets.tablets_HP_PRO()
        self.product.plus().click()  # add quantity
        self.product.plus().click()  # add quantity
        self.product.plus().click()  # add quantity
        self.product.add_to_cart().click()  # add to cart
        text1 =self.main.miniCartTable(2, 1).text
        self.assertIn("HP ELITEPAD 1000 G2", text1) #name
        self.assertIn("BLUE", text1) #color
        self.assertIn("QTY: 2", text1) #quantity
        price1 = self.main.miniCartTable(2, 2).text
        self.assertIn("$2,018.00", price1)  # price
        text2=self.main.miniCartTable(1,1).text
        self.assertIn("HP ELITE X2 1011 G1", text2)  # name
        self.assertIn("BLACK", text2)  # color
        self.assertIn("QTY: 3", text2)  # quantity
        price2=self.main.miniCartTable(1, 2).text
        self.assertIn("$3,837.00", price2)  # price
        text3 =self.main.miniCartTable(0, 1).text
        self.assertIn("HP PRO TABLET 608 G1", text3)  # name
        self.assertIn("BLACK", text3)  # color
        self.assertIn("QTY: 4", text3)  # quantity
        # need to check why price3 in not readen to fix this check <<-----------
        price3 = self.main.miniCartTable(0, 2).text
        self.assertIn("$1,916.00", price3)  # price








