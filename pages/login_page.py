from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure

class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    USERNAME_INPUT = By.CSS_SELECTOR, "input[id='user-name']"
    PASSWORD_INPUT = By.CSS_SELECTOR, "input[type='password']"
    LOGIN_BUTTON = By.CSS_SELECTOR, "input[type='submit']"

    @allure.step("Enter Login")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_INPUT)).click()
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_INPUT)).send_keys(login)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT)).click()
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT)).send_keys(password)

    @allure.step("Click login button")
    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
