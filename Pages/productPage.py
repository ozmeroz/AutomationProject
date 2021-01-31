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
        self.driver.find_element_by_css_selector("button[translate='ADD_TO_CART']").click()

    def ex_num(self,string):
       num=[]
       for char in string:
        pass

    def savedetails(self):
        'function that returns list with full name and price of specipic product'
        details=[]
        details.append(self.driver.find_element_by_css_selector("h1.screen768").text)
        price=self.driver.find_element_by_css_selector("h2.screen768").text
        list(price) #cast price to list
        newprice='' #empty string
        for i in price:
            if i.isnumeric() or i=='.':  #takes only numbers and '.'
                newprice+=str(i)
        newprice=float(newprice)
        details.append(newprice)
        return details




