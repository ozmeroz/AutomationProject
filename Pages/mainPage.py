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
        'function that returns the user menu icon element'
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#see_offer_btn"))) # wait until page loads
        element=self.driver.find_element_by_css_selector("#menuUser")
        return element

    def usernameField(self):
        'function that fills our username'
        return self.driver.find_element_by_css_selector("input[name='username']").send_keys("tomoz")

    def passwordField(self):
        'function that fills out password'
        return self.driver.find_element_by_css_selector("input[name='password']").send_keys("tomOz123")

    def signInBtn(self):
        'function that returns the signIn button element'
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[id='sign_in_btnundefined']")))
        return self.driver.find_element_by_css_selector("button[id='sign_in_btnundefined']")

    def loggedUserName(self):
        'fucntion that reads the current logged username and returns it as text'
        return self.driver.find_element_by_css_selector("span.hi-user:nth-child(1)").text

    def signedUserElement(self):
        'function that returns the element of user menu'
        return self.driver.find_element_by_css_selector("span[class='hi-user containMiniTitle ng-binding']")

    def logOut(self):
        'function that clicks the usermenu and than clicks signout button'
        self.signedUserElement().click()
        self.driver.find_element_by_xpath("//li[3]/a/div/label[3]").click()

    def getHeaderElements(self):
        return self.driver.find_elements_by_css_selector("header[ng-show='welcome']")

    def jump_to_category(self,category_name):
        'function that gets the categoty name and jumps to that category from main page'
        self.driver.find_element_by_css_selector(f"div#{category_name}Img").click()

    def endtest(self):
        'this function will be used at the teardown, will leave us 2 seconds to see the home page before it quits'
        self.driver.find_element_by_css_selector(".logo").click()
        time.sleep(2) #just to see the home page before it closes
        self.driver.close()

    def hoverCart(self):
        'function to hover with the mouse over the mini cart icon'
        element_to_hover= self.driver.find_element_by_id("menuCart")
        hover = self.actions.move_to_element(element_to_hover)
        hover.perform()

    def enterCartPage(self):
        'opens the cartpage menu'
        self.driver.find_element_by_css_selector("#shoppingCartLink").click()

    def product_color_black(self):
        'returns black color element'
        return self.driver.find_element_by_class("BLACK")

    def checkTotalItems(self):
        'function that opens the minicart and return the total items as text'
        self.hoverCart()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ng-binding>label")))
        total=self.driver.find_element_by_css_selector(".ng-binding>label").text
        return total

    def miniCartTable(self, rowindex, cellindex):
        'func that gets row num and cell num and returns the element in this place'
        self.hoverCart()
        table=self.driver.find_element_by_xpath("//tool-tip-cart/div/table")
        rows = table.find_elements_by_tag_name("tr")
        for row in rows:
            if rows.index(row) == rowindex:
                cells = row.find_elements_by_tag_name("td")
                for cell in cells:
                    if cells.index(cell)==cellindex:
                        return cell


    def miniCart(self):
        'function that gets the table by row texts, one row to index'
        list = []
        self.hoverCart()
        table = self.driver.find_element_by_xpath("//tool-tip-cart/div/table")
        rows = table.find_elements_by_tag_name("tr")
        for row in rows:
            list.append(row.text)
        return list

    def remove_from_minicart(self):
        'returns the element of remove icon from mini cart'
        return self.driver.find_element_by_class_name("removeProduct")

    def enterMyOrders(self):
        'function that enters my orders page'
        self.driver.find_element_by_id("menuUser").click()
        self.wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, ".emptyCart")))
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#loginMiniTitle > label:nth-child(2)")))
        self.driver.find_element_by_css_selector("#loginMiniTitle > label:nth-child(2)").click()

    def populer_items(self):
        'get the text out of populer items in the main page'
        return self.driver.find_element_by_css_selector('h3[translate="POPULAR_ITEMS"]').text


