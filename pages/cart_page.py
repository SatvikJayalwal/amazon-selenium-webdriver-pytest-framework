from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self,driver):
        self.driver=driver
    
    def open_cart(self):
        #open the Shopping Cart
        self.driver.find_element(By.XPATH,"//span[@id='nav-cart-count']").click()

    def get_cart_count(self):
        return len(self.driver.find_elements(By.XPATH, "//span[contains(@class,'sc-product-title')]"))
