from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    def __init__(self,driver):
        self.driver=driver

    def search_product(self,product):

        #wait for the searchbox to load
        search_box=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='twotabsearchtextbox']")))

        #clear the search box and write the product name and hit the enter key
        search_box.clear() 
        print(f"SEARCHING FOR: {product}") #print product name being searched in the terminal
        search_box.send_keys(product + Keys.ENTER) 