import time
from pages.home_page import HomePage
from pages.results_page import ResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_add_products_to_cart(driver,product_list):

    #creating objects for every class and passing driver in them
    home=HomePage(driver)
    results=ResultsPage(driver)
    product_page=ProductPage(driver)
    cart=CartPage(driver)

    for item in product_list:
        print(f"SEARCHING FOR : {item}")
        home.search_product(item)
        results.click_second_result()
        product_page.add_to_cart()
        print(f"ADDED TO CART : {item}")
        product_page.handle_warranty_popup()

    #define expected_count and actual_count
    cart.open_cart()
    actual_count=cart.get_cart_count()
    expected_count=len(product_list)
    
    #assert expected_count and actual_count
    assert actual_count == expected_count, "CART COUNT MISMATCH !!"
    print("CART VERIFICATION PASSED")
    time.sleep(2)





    



