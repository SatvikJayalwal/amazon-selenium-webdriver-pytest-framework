import pytest
from utils.driver_factory import create_driver
import pandas as pd

@pytest.fixture
def driver():

    driver=create_driver()
    #opening website
    driver.get("https://www.amazon.in/")    
    yield driver

    #quit driver
    driver.quit()   


@pytest.fixture
def product_list():
    #read Products from excel sheet 
    # products=pd.read_excel("C:\\python_codes\\AutomatingAmazon\\data\\products.xlsx")["Products"]
    df = pd.read_excel("data/products.xlsx")
    return df["Products"].tolist()