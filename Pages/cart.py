from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
class Cart:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(driver, 10)

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
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='next_btn']")))
        self.driver.find_element_by_css_selector("button[id='next_btn']").click()
        self.driver.find_element_by_name("safepay_username").send_keys("tomozsafepay")
        self.driver.find_element_by_name("safepay_password").send_keys("To1234")
        self.wait.until(EC.element_to_be_clickable((By.ID, "pay_now_btn_SAFEPAY")))
        self.driver.find_element_by_id("pay_now_btn_SAFEPAY").click()

    def fill_creditCard(self):
        self.driver.find_element_by_id("creditCard").send_keys("123456789012")
        self.driver.find_element_by_name("cvv_number").send_keys("123")
        self.driver.find_element_by_name("cvv_number").clear()
        self.driver.find_element_by_name("cvv_number").send_keys("234")
        mm = Select(self.driver.find_element_by_name("mmListbox"))
        mm.select_by_index(7)
        yy = Select(self.driver.find_element_by_name("yyyyListbox"))
        yy.select_by_index(7)
        self.driver.find_element_by_name("cardholder_name").send_keys("Tom Oz")
        self.driver.find_element_by_name("save_master_credit").click()
        self.wait.until(EC.element_to_be_clickable((By.ID, "pay_now_btn_ManualPayment")))
        self.driver.find_element_by_id("pay_now_btn_ManualPayment").click()