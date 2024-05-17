from base.base_test import BaseTest
import allure
import pytest


@allure.feature("Adding an product or products to cart")
class TestAddProductsToBasketTest(BaseTest):

    @allure.title('Adding one any product to cart')
    @allure.severity("High")
    @pytest.mark.smoke
    def test_add_product_to_basket(self):
        self.login_page.open_page()
        self.login_page.is_opened()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login_button()
        self.products_carts_page.is_opened()
        self.products_carts_page.click_product_cart(card_number=0)
        self.product_detail_cart_page.click_add_button()
        product_name_in_detail_cart = self.product_detail_cart_page.get_product_name_text()
        product_price_in_detail_cart = self.product_detail_cart_page.get_product_price_text()
        self.product_detail_cart_page.make_screenshot("Product to be added to cart")
        self.basket_page.go_too_basket()
        self.basket_page.is_opened()
        product_name_in_basket = self.basket_page.get_product_name_text()
        product_price_in_basket = self.basket_page.get_product_price_text()
        with allure.step("Checking that the product has been added to the cart "
                         "the name and price of the product correspond to what was added"):
            assert product_name_in_detail_cart == product_name_in_basket
            assert product_price_in_detail_cart == product_price_in_basket
            self.basket_page.make_screenshot("Success")
