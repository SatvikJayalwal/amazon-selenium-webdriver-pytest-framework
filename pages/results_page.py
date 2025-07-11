from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResultsPage:

    def __init__(self,driver):
        self.driver=driver

    def click_second_result(self):
        #wait for the page to load 
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'s-main-slot')]")))

        #click the product card with index 3 and ignore sponser product cards
        search_results = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(@data-component-type,'s-search-result') and not(.//span[contains(text(),'Sponsored')])])[2]//h2/ancestor::a")))
        search_results.click()

