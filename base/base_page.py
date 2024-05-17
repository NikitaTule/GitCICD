import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    BASKET_BUTTON = By.CSS_SELECTOR, "div>a.shopping_cart_link"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open_page(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def go_too_basket(self):
        self.wait.until(EC.element_to_be_clickable(self.BASKET_BUTTON)).click()

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )
