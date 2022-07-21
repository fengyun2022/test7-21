from selenium.webdriver.common.by import By

class Loginpage:
    def __init__(self,driver):
        self.driver=driver
        self.loginuser=By.CSS_SELECTOR, "[name='account']"
        self.loginpass=By.CSS_SELECTOR, "[name='password']"
        self.loginbutton=By.CSS_SELECTOR, '#submit'

    def input_user(self,username):
        self.driver.find_element(*self.loginuser).send_keys(username)

    def input_pass(self,password):
        self.driver.find_element(*self.loginpass).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.loginbutton).click()


