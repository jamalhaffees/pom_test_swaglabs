from pages.LoginPage import LoginPage
from pages.ProductListPage import ProductListPage
from utilities.Logger import Logger

class TestProductList:

    # class attributes
    logger = Logger.get_logger()

    # class methods = test cases
    def test_add_to_cart(self, setup):
        self.logger.info('********** Test Case: Add to Cart')
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.add_to_cart()
        if self.product_list_page.product_added():
            assert True
        else:
            assert False
    
    def test_view_produc_details(self, setup):
        self.logger.info('********** Test Case: View Product Details')
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.view_product_details()
        if 'back to products' in self.driver.page_source.lower():
            assert True
        else:
            assert False