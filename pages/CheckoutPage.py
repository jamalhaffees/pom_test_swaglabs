from selenium.webdriver.common.by import By

class CheckoutPage:
    button_checkout_css = '#checkout'
    

     # class constructor, initializer
    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_checkout_css).click()