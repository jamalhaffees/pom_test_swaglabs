from pages.LoginPage import LoginPage
from pages.ProductListPage import ProductListPage

from pages.CartPage import CartPage
from utilities.Logger import Logger

class TestCart:

    # class attributes
    logger = Logger.get_logger()


      # class methods = test cases
    def test_shopping_cart(self, setup):
       
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.add_to_cart()
        self.logger.info('********** Test Case: Shopping cart details')
        self.cart_page = CartPage(self.driver)
        self.cart_page.click_shopping_cart()
        if 'cart' in self.driver.page_source.lower():
            assert True
        else:
            assert False

   

    def test_click_remove(self, setup):
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.add_to_cart()
        self.cart_page = CartPage(self.driver)
        self.cart_page.click_shopping_cart()
        self.logger.info('********** Test Case: Empty shopping cart')
        self.cart_page.click_remove()
        page_source =self.driver.page_source
        if '1' in self.driver.page_source.lower():
            assert True
        else:
            assert False

   

    # def test_continue_shopping_button(self, setup):
    
    #     self.driver = setup
    #     self.login_page = LoginPage(self.driver)
    #     self.login_page.valid_login()
    #     self.product_list_page = ProductListPage(self.driver)
    #     self.product_list_page.add_to_cart()
    #     self.cart_page = CartPage(self.driver)
    #     self.cart_page.click_continue_shopping()
    #     if 'products page' in self.driver.page_source.lower() :
    #         assert True
    #     else:
    #         assert False

    # def test_checkout_button(self, setup):
    #     self.driver = setup
    #     self.login_page = LoginPage(self.driver)
    #     self.login_page.valid_login()
    #     self.product_list_page = ProductListPage(self.driver)
    #     self.product_list_page.add_to_cart()
    #     self.cart_page = CartPage(self.driver)
    #     self.cart_page.click_checkout()
    
