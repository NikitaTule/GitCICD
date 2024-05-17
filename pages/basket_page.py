from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_static_metots import StaticMetods


class BasketPage(BasePage):
    PAGE_URL = Links.BASKET_PAGE

    PRODUCT_NAME = By.CSS_SELECTOR, "div.inventory_item_name"
    PRODUCT_PRICE = By.CSS_SELECTOR, "div.inventory_item_price"

    def get_product_name_text(self):
        product_name = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_NAME))
        return StaticMetods.get_text_from_webelement(product_name)

    def get_product_price_text(self):
        product_price = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_PRICE))
        return StaticMetods.get_text_from_webelement(product_price)

