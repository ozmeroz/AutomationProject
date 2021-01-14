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
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(driver, 10)

    def usermenu(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#see_offer_btn"))) # wain until page loads
        element=self.driver.find_element_by_css_selector("#menuUser")
        return element
    def usernameField(self):
        return self.driver.find_element_by_css_selector("input[name='username']").send_keys("tomoz")
    def passwordField(self):
        return self.driver.find_element_by_css_selector("input[name='password']").send_keys("tomOz123")
    def signInBtn(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[id='sign_in_btnundefined']")))
        return self.driver.find_element_by_css_selector("button[id='sign_in_btnundefined']")
    def loggedUserName(self):
        return self.driver.find_element_by_css_selector("span.hi-user:nth-child(1)").text
    def signedUserElement(self):
        return self.driver.find_element_by_css_selector("span[class='hi-user containMiniTitle ng-binding']")
    def logOut(self):
        self.signedUserElement().click()
        self.driver.find_element_by_xpath("//li[3]/a/div/label[3]").click()
    def getHeaderElements(self):
        return self.driver.find_elements_by_css_selector("header[ng-show='welcome']")

    def endtest(self):
        self.driver.find_element_by_css_selector(".logo").click()
        time.sleep(2)
        self.driver.close()

    def hoverCart(self):
        element_to_hover= self.driver.find_element_by_id("menuCart")
        hover = self.actions.move_to_element(element_to_hover)
        hover.perform()

    def tablets(self):
        return self.driver.find_element_by_id("tabletsImg")
           #טאבלטים
    def tablets_elitepad(self):
        'jumps to the specific product page'
        return self.driver.get("https://www.advantageonlineshopping.com/#/product/16")

    def tablets_HPelite(self):
        'jumps to the specific product page'
        return self.driver.get("https://www.advantageonlineshopping.com/#/product/17")

    def tablets_HP_PRO(self):
        'jumps to the specific product page'
        return self.driver.get("https://www.advantageonlineshopping.com/#/product/18")
    #אליטפד פנימי
    def elitepad_color_blue(self):
        return self.driver.find_element_by_class("BLUE")

    def product_color_gray(self):
        return self.driver.find_element_by_class("GRAY")

    def plus(self):
        return self.driver.find_element_by_css_selector("div[class='plus']")

    def minus(self):
        return self.driver.find_element_by_css_selector("div[class='minus']")

    def add_to_cart(self):
        return self.driver.find_element_by_css_selector("button[translate='ADD_TO_CART']")

    def elitpad_to_tablets(self):
        return self.driver.find_element_by_css_selector("div.uiview>nav>a.ng-scope")

    def product_color_black(self):
        return self.driver.find_element_by_class("BLACK")

    def checkTotalItems(self):
        self.hoverCart()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ng-binding>label")))
        total=self.driver.find_element_by_css_selector(".ng-binding>label").text
        return total

    def miniCartTable(self, rowindex, cellindex):
        'func that gets row num and cell num and returns the element in this place'
        self.hoverCart()
        #self.driver.find_element_by_css_selector("table[ng-show='cart.productsInCart.length > 0']")
        table=self.driver.find_element_by_xpath("//tool-tip-cart/div/table")
        rows = table.find_elements_by_tag_name("tr")
        for row in rows:
            if rows.index(row)==rowindex:
                cells = row.find_elements_by_tag_name("td")
                for cell in cells:
                    if cells.index(cell)==cellindex:
                        return cell






