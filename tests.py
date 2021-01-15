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
        self.product.jumpToProductPage(16) #enter specific product
        self.product.plus(1).click() #add quantity
        self.product.add_to_cart().click() #add to cart
        self.product.jumpToProductPage(17) #enter specific product
        self.product.plus(2).click() #add quantity
        self.product.add_to_cart().click() #add to cart
        self.main.hoverCart() #hover over cart button to open cart summary
        self.assertIn("5", self.main.checkTotalItems())

    def test_ex2(self):
        self.category.tablets_category().click()  # enter tablets category
        self.product.jumpToProductPage(16)  # enter specific product
        self.product.plus(1).click()  # add quantity
        self.product.add_to_cart().click()  # add to cart
        self.product.jumpToProductPage(17)  # enter specific product
        self.product.plus(2).click()  # add quantity
        self.product.add_to_cart().click()  # add to cart
        self.product.jumpToProductPage(18) # enter specific product
        self.product.plus(3).click()  # add quantity

        self.product.add_to_cart().click()  # add to cart
        list_pro = self.main.miniCart()
        self.assertIn("HP ELITEPAD 1000 G2", list_pro[2]) #name
        self.assertIn("BLUE", list_pro[2]) #color
        self.assertIn("QTY: 2", list_pro[2]) #quantity
        self.assertIn("$2,018.00", list_pro[2]) #price
        self.assertIn("HP ELITE X2 1011 G1", list_pro[1])  # name
        self.assertIn("BLACK", list_pro[1])  # color
        self.assertIn("QTY: 3", list_pro[1])  # quantity
        self.assertIn("$3,837.00", list_pro[1])  # price
        self.assertIn("HP PRO TABLET 608 G1", list_pro[0])  # name
        self.assertIn("BLACK", list_pro[0])  # color
        self.assertIn("QTY: 4", list_pro[0])  # quantity
        self.assertIn("$1,916.00", list_pro[0])  # price

    def test_ex3(self):
        self.category.tablets_category().click()  # enter tablets category
        self.tablets.tablets_elitepad()  # enter specific product
        self.product.add_to_cart().click()  # add to cart
        self.tablets.tablets_HPelite()  # enter specific product
        self.product.plus(2).click()  # add quantity
        self.product.add_to_cart().click()  # add to cart
        self.main.hoverCart()
        self.main.remove_from_minicart().click()
        prodname =self.main.miniCartTable(0, 1).text
        self.assertNotEqual(prodname,"HP ELITE X2 1011 G1 TABLET ")


    def test_ex_4(self):
        self.product.jumpToProductPage(7)
        self.product.add_to_cart().click()
        self.main.enterCartPage().click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#checkOutButton"))) #helps to wait for page to load
        currentPage =self.driver.find_element_by_xpath("//nav/a[2]").text
        self.assertTrue(currentPage=="SHOPPING CART")

    def test_ex_5(self):
        self.product.jumpToProductPage(16) # specific product
        self.product.plus(3)
        self.product.add_to_cart().click()
        self.product.jumpToProductPage(17)
        self.product.plus(2)
        self.product.add_to_cart().click()
        self.product.jumpToProductPage(18)
        self.product.plus(5)
        self.product.add_to_cart().click()

    def test_ex10(self):
        self.main.usermenu().click() #login
        self.main.usernameField() #login
        self.main.passwordField() #login
        self.main.signInBtn().click() #login
        signeduser=self.main.signedUserElement()
        self.assertTrue("tomoz"==signeduser.text) #check if signed user is our username
        self.main.logOut() #click logout
        self.assertNotIn(signeduser, self.main.getHeaderElements()) #check if signeduser name is not in all Header Elements list


















