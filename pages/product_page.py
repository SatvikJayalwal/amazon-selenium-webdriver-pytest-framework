from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:

    def __init__(self,driver):
        self.driver=driver

    def add_to_cart(self):
        #click add to cart button 
        add_to_cart_btn=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'a-section') and contains(@class,'a-padding-none')]//input[@id='add-to-cart-button']")))    
        add_to_cart_btn.click()
        
    def handle_warranty_popup(self):
        #handle warranty side pop-up
        try : 
            
            warranty_skip_btn=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//span[@id='attachSiNoCoverage']//input[@type='submit']")))
            warranty_skip_btn.click()
            print("WARRANTY POP-UP SKIPPED BUTTON CLICKED")

            WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located((By.XPATH,"//*[@id='attach-desktop-sideSheet' or @id='attach-accessory-pane']")))
            print("WARRANTY POP-UP DISMISSED")

        except :
            pass

        
        
