from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure


class ProductsCartsPage(BasePage):

    PAGE_URL = Links.PRODUCTS_PAGE

    PRODUCT_CARDS = By.CSS_SELECTOR, "div > div.inventory_item_img"

    @allure.step("Go to detailed product card")
    def click_product_cart(self, card_number):
        product_cart = self.wait.until(EC.visibility_of_all_elements_located(self.PRODUCT_CARDS))
        product_cart[card_number].click()
