from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
class Tablets:

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(driver, 10)

    def tablets_elitepad(self):
        'jumps to the specific product page'
        return self.driver.get("https://www.advantageonlineshopping.com/#/product/16")

    def tablets_HPelite(self):
        'jumps to the specific product page'
        return self.driver.get("https://www.advantageonlineshopping.com/#/product/17")

    def tablets_HP_PRO(self):
        'jumps to the specific product page'
        return self.driver.get("https://www.advantageonlineshopping.com/#/product/18")