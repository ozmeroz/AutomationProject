from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(driver, 10)


    def plus(self,qunt):
        for times in range(qunt):
            self.driver.find_element_by_css_selector("div[class='plus']").click()

    def minus(self,qunt):
        for i in range(qunt):
            self.driver.find_element_by_css_selector("div[class='minus']").click()

    def add_to_cart(self):
        return self.driver.find_element_by_css_selector("button[translate='ADD_TO_CART']")

    def jumpToProductByImage(self, id):
        self.driver.find_element_by_css_selector(f"img[id='{id}']").click()
