from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def usermenu(self):
        return self.driver.find_element_by_css_selector("#menuUser")
    def usernameField(self):
        return self.driver.find_element_by_css_selector("input[name='username']").send_keys("tomoz")
    def passwordField(self):
        return self.driver.find_element_by_css_selector("input[name='password']").send_keys("tomOz123")
    def signInBtn(self):
        return self.driver.find_element_by_css_selector("button[id='sign_in_btnundefined']")
    def loggedUserName(self):
        return self.driver.find_element_by_css_selector("span.hi-user:nth-child(1)").text

