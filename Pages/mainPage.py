from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
class mainPage:




    def usermenu(self):
        return self.driver.find_element_by_css_selector("#menuUser")
    def usernameField(self):
        return self.driver.find_element_by_css_selector(".ng-touched").send_keys("tomoz")
    def passwordField(self):
        return self.driver.find_element_by_css_selector("input[name = 'password']").send_keys("tomOz123")
    def SignInBtn(self):
        return self.driver.find_element_by_css_selector("#sign_in_btnundefined")
           #טאבלטים
    def tablets(self):
        return self.driver.find_element_by_id("tabletsImg")

    def tablets_elitepad(self):
        return self.driver.find_element_by_id('img[id="16"]')

    def tablets_HPelite(self):
        return self.driver.find_element_by_id('img[id="17"]')

    def tablets_HP_PRO(self):
        return self.driver.find_element_by_id('img[id="18"]')

    def elitepad_color_blue(self):
        return self.driver.find_element_by_class("span.BLUE")

    def elitepad_color_gray(self):
        return self.driver.find_element_by_class("span.GRAY")


