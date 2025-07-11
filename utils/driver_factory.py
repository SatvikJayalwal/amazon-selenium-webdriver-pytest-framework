from selenium import webdriver

def create_driver():

    #chrome options settings
    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--ignore_certificate_errors")
    chrome_options.add_argument("--incognito")
    driver=webdriver.Chrome(options=chrome_options)
    return driver
