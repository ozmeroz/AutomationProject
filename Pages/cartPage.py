from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from Pages.mainPage import MainPage
class Cart:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(driver, 10)
        self.main=MainPage(self.driver)

    def cart(self):
        self.driver.find_element_by_id("menuCart")

    def checkout(self):
        time.sleep(2)
        self.driver.find_element_by_id("checkOutButton").click()

    def fill_username_in_order(self, username):
        self.driver.find_element_by_name("usernameInOrderPayment").send_keys(username)

    def fill_password_in_order(self, password):
        self.driver.find_element_by_name("passwordInOrderPayment").send_keys(password)

    def click_login_in_order(self):
        self.driver.find_element_by_id("login_btnundefined").click()

    def next_btn_in_order(self):
        self.driver.find_element_by_id("next_btn").click()

    def select_masterCredit(self):
        self.driver.find_element_by_css_selector("input[name='masterCredit']").click()

    def newUserRegBtn(self):
        self.driver.find_element_by_id("registration_btnundefined").click()

    def fillNewUserForm(self):
        self.driver.find_element_by_name("usernameRegisterPage").send_keys("tomoz")
        self.driver.find_element_by_name("passwordRegisterPage").send_keys("tomOz123")
        self.driver.find_element_by_name("confirm_passwordRegisterPage").send_keys("tomOz123")
        self.driver.find_element_by_name("emailRegisterPage").send_keys("tom@project.oz")
        self.driver.find_element_by_name("first_nameRegisterPage").send_keys("tom")
        self.driver.find_element_by_name("last_nameRegisterPage").send_keys("Oz")
        self.driver.find_element_by_name("phone_numberRegisterPage").send_keys("052123456789")
        country = Select(self.driver.find_element_by_name("countryListboxRegisterPage"))
        country.select_by_visible_text("Israel")
        self.driver.find_element_by_name("cityRegisterPage").send_keys("Tel Aviv")
        self.driver.find_element_by_name("addressRegisterPage").send_keys("Yigal Alon 90")
        self.driver.find_element_by_name("state_/_province_/_regionRegisterPage").send_keys("Tel Aviv")
        self.driver.find_element_by_name("postal_codeRegisterPage").send_keys("1020300")
        self.driver.find_element_by_css_selector("input[name='i_agree']").click()
        self.wait.until(EC.element_to_be_clickable((By.ID, "register_btnundefined")))
        self.driver.find_element_by_id("register_btnundefined").click()

    def paybySafepay(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='next_btn']")))
        self.driver.find_element_by_css_selector("button[id='next_btn']").click()
        self.driver.find_element_by_name("safepay_username").send_keys("tomozsafepay")
        self.driver.find_element_by_name("safepay_password").send_keys("To1234")
        self.wait.until(EC.element_to_be_clickable((By.ID, "pay_now_btn_SAFEPAY")))
        self.driver.find_element_by_id("pay_now_btn_SAFEPAY").click()

    def checkIfOrderSucceed(self):
        'function that checks if order suceed, if yes - returns the order number, else returns false'
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span[translate='Thank_you_for_buying_with_Advantage']")))
        element=self.driver.find_element_by_css_selector("span[translate='Thank_you_for_buying_with_Advantage']")
        if element.text=="Thank you for buying with Advantage":
            return self.driver.find_element_by_id("orderNumberLabel").text
        else:
            return False
    def checkIfCartIsEmpty(self):
        'returns True for empty cart, False if cart is not empty'
        self.main.hoverCart()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".emptyCart")))
        cartext = self.driver.find_element_by_css_selector(".emptyCart").text
        if "empty" in cartext:
            return True
        else:
            return False

    def fill_creditCard(self):
        'func that fills card input fields and clicks paynow button'
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='card_number']"))).click()
        self.driver.find_element_by_css_selector("input[name='card_number']").send_keys("123456789012")
        self.driver.find_element_by_css_selector("input[name='cvv_number']").send_keys("123")
        self.driver.find_element_by_css_selector("input[name='cvv_number']").clear()
        self.driver.find_element_by_css_selector("input[name='cvv_number']").send_keys("234") #double fill to bypass the bug that skips the first digit
        mm = Select(self.driver.find_element_by_name("mmListbox"))
        mm.select_by_index(7)
        yy = Select(self.driver.find_element_by_name("yyyyListbox"))
        yy.select_by_index(7)
        self.driver.find_element_by_name("cardholder_name").send_keys("Tom Oz")
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='card_number']"))).clear()
        self.driver.find_element_by_css_selector("input[name='card_number']").send_keys("123456789013")
        self.wait.until(EC.element_to_be_clickable((By.ID, "pay_now_btn_ManualPayment")))
        self.driver.find_element_by_id("pay_now_btn_ManualPayment").click()

    def edit_from_cart(self,btn_num):
        "chooses which product you want to edit from the shopping cart"
        edit_list=(self.driver.find_elements_by_css_selector("a.edit"))
        btn_num-=1

        return edit_list[btn_num]

    def get_quntity_by_row(self ,rownum):
        'function that gets row number and return the quantity in text'
        return self.driver.find_element_by_xpath(f"//tr[{rownum}]/td[5]/label[2]").text

    def dealTotalPrice(self):
        'function that returns the total price from cart page without (,) between digits'
        total = self.driver.find_element_by_xpath("//td[2]/span[2]").text  # total price from cart page
        total = list(total)
        total.pop(2) # pop out the ','
        total = ''.join(total)
        return total
