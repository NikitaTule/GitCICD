import pytest

from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.products_carts_page import ProductsCartsPage
from pages.product_detail_cart_page import ProductDetailPage
from config.data import Data


class BaseTest:
    data: Data
    login_page: LoginPage
    basket_page: BasketPage
    products_carts_page: ProductsCartsPage
    product_detail_cart_page: ProductDetailPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data
        request.cls.login_page = LoginPage(driver)
        request.cls.basket_page = BasketPage(driver)
        request.cls.products_carts_page = ProductsCartsPage(driver)
        request.cls.product_detail_cart_page = ProductDetailPage(driver)
