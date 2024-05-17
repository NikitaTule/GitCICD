from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_static_metots import StaticMetods
import allure


class ProductDetailPage(BasePage):
    ADD_TO_BASKET_BUTTON = By.CSS_SELECTOR, "div > button[data-test='add-to-cart']"
    PRODUCT_NAME = By.CSS_SELECTOR, "div.inventory_details_name"
    PRODUCT_PRICE = By.CSS_SELECTOR, "div.inventory_details_price"

    @allure.step("Add product to cart")
    def click_add_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_BASKET_BUTTON)).click()

    @allure.step("Saving or remember  the product name")
    def get_product_name_text(self):
        product_name = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_NAME))
        return StaticMetods.get_text_from_webelement(product_name)

    @allure.step("Saving or remember the price of the product")
    def get_product_price_text(self):
        product_price = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_PRICE))
        return StaticMetods.get_text_from_webelement(product_price)
