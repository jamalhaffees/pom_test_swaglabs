from pages.LoginPage import LoginPage
from pages.ProductListPage import ProductListPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from utilities.Logger import Logger

class TestCheckout:

    # class attributes
    logger = Logger.get_logger()

    def test_checkout_button(self, setup):
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.add_to_cart()
        self.cart_page = CartPage(self.driver)
        self.cart_page.click_shopping_cart()
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_page.click_checkout()
        if 'checkout' in self.driver.page_source.lower():
            assert True
        else:
            assert False