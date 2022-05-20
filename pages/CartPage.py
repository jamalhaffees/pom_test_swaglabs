from selenium.webdriver.common.by import By

class CartPage:
    
    # class attributes
    text_shopping_cart_css= '.shopping_cart_link'
   
    button_click_remove_css = '#remove-sauce-labs-backpack'
    
   
    # class constructor, initializer
    def __init__(self, driver):
        self.driver = driver
    
    # # class method, actions, behavior
    def click_shopping_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.text_shopping_cart_css).click()

    #
    
    
    def click_remove(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_click_remove_css).click()
        
    
     # button_continue_shopping_css = '#continue-shopping'
    # button_checkout_css = '#checkout'
    # text_item_price_css = '.inventory_item_price'

    # def click_continue_shopping(self):
    #     self.driver.find_element(By.CSS_SELECTOR, self.button_continue_shopping_css).click()

    # def click_checkout(self):
    #     self.driver.find_element(By.CSS_SELECTOR, self.button_checkout_css).click()

    # def item_price(self):
    #     self.driver.find_element(By.CSS_SELECTOR, self.text_item_price_css).click()