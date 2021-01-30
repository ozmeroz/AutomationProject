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


class Order:

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(driver, 10)
        self.main=MainPage(self.driver)

    def ordersTableRowsText(self):
        'function that returns orders table text'
        table = self.driver.find_element_by_css_selector(".cover > table")
        return table.text