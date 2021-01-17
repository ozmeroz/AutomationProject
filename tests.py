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
from Pages.cart import Cart
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
        self.cart = Cart(self.driver)

    def tearDown(self):
       self.main.endtest()


    def test_ex1(self):
        self.main.jump_to_category("tablets") #enter tablets category
        self.category.jumpToProductByImage(16) #enter specific product
        self.product.plus(1) #add quantity
        self.product.add_to_cart().click() #add to cart
        self.driver.back()
        self.category.jumpToProductByImage(17) #enter specific product
        self.product.plus(2) #add quantity
        self.product.add_to_cart().click() #add to cart
        self.main.hoverCart() #hover over cart button to open cart summary
        self.assertIn("5", self.main.checkTotalItems())

    def test_ex2(self):
        self.main.jump_to_category("tablets")  # enter tablets category
        self.category.jumpToProductByImage(16)   # enter specific product
        self.product.plus(1)  # add quantity
        self.product.add_to_cart().click()  # add to cart
        self.driver.back()
        self.category.jumpToProductByImage(17)   # enter specific product
        self.product.plus(2)  # add quantity
        self.product.add_to_cart().click()  # add to cart
        self.driver.back()
        self.category.jumpToProductByImage(18)   # enter specific product
        self.product.plus(3)  # add quantity
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
        self.main.jump_to_category("tablets")  # enter tablets category
        self.category.jumpToProductByImage(16)  # enter specific product
        self.product.add_to_cart().click()  # add to cart
        self.driver.back()   # back to tablets category
        self.category.jumpToProductByImage(17)  # enter specific product
        self.product.plus(2)  # add quantity
        self.product.add_to_cart().click()  # add to cart
        self.main.hoverCart()
        self.main.remove_from_minicart().click()
        prodname =self.main.miniCartTable(0, 1).text
        products_in_cart=self.main.miniCart()
        print(products_in_cart)
        self.assertNotEqual(prodname,"HP ELITE X2 1011 G1 TABLET ")
        'הפונקציה עובדת, אפשר לנסות לשפר ולהשתמש במיניקארט החדשה במקום בפונקציה הארוכה'


    def test_ex_4(self):
        self.driver.find_element_by_css_selector("#laptopsImg").click()
        self.category.jumpToProductByImage(7)    # enter specific product
        self.product.add_to_cart().click()
        self.main.enterCartPage()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#checkOutButton"))) #helps to wait for page to load
        currentPage =self.driver.find_element_by_xpath("//nav/a[2]").text
        self.assertTrue(currentPage=="SHOPPING CART")

    def test_ex_5(self):
        self.main.jump_to_category("tablets")  # enter tablets category
        self.category.jumpToProductByImage(16)   # enter specific product
        self.product.plus(3)    #add quantity
        self.product.add_to_cart().click()
        self.driver.back()  #back to tablets page
        self.category.jumpToProductByImage(17)   # enter specific product
        self.product.plus(2)    #add quantity
        self.product.add_to_cart().click()
        self.driver.back()  #back to tablets page
        self.category.jumpToProductByImage(18)   # enter specific product
        self.product.plus(5)    #add quantity
        self.product.add_to_cart()
        prod_list=self.main.miniCart()
        print(prod_list)
        prod_list=str(prod_list)
        print(prod_list.split("\n"))





    def test_ex8(self):
        self.main.jump_to_category("headphones")
        self.category.jumpToProductByImage(15)
        self.product.add_to_cart()
        self.main.enterCartPage()
        self.cart.checkout()
        self.cart.newUserRegBtn() #clicks registration for new user
        self.cart.fillNewUserForm()
        self.cart.paybySafepay()
        time.sleep(5)
        ordernumber = self.cart.checkIfOrderSucceed() #returns order number if payment was successfull / return false if payment didnt made successfully
        self.assertNotEqual(ordernumber,False) #check if payment made successfully
        self.assertTrue(self.cart.checkIfCartIsEmpty()==True) #checks if cart is empty
        self.main.enterMyOrders()
        self.assertIn(ordernumber, self.order.ordersTableRowsText()) # checks if order number is in orders table of the user




    def test_ex9(self):
        self.main.jump_to_category("mice")
        self.category.jumpToProductByImage(33)
        self.product.add_to_cart()
        self.main.enterCartPage()
        self.cart.checkout()
        self.cart.fill_username_in_order("tomoz")
        self.cart.fill_password_in_order("tomOz123")
        self.cart.click_login_in_order()
        self.cart.next_btn_in_order()
        self.cart.select_masterCredit()
        self.cart.fill_creditCard()
        ordernumber = self.cart.checkIfOrderSucceed()  # returns order number if payment was successfull
        self.assertTrue(self.cart.checkIfCartIsEmpty() == True)  # checks if cart is empty
        self.main.enterMyOrders()
        self.assertIn(ordernumber, self.order.ordersTableRowsText())  # checks if order number is in orders table of the user


    def test_ex10(self):
        self.main.usermenu().click() #login
        self.main.usernameField() #login
        self.main.passwordField() #login
        self.main.signInBtn().click() #login
        signeduser=self.main.signedUserElement()
        self.assertTrue("tomoz"==signeduser.text) #check if signed user is our username
        self.main.logOut() #click logout
        self.assertNotIn(signeduser, self.main.getHeaderElements()) #check if signeduser name is not in all Header Elements list


















