from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import pytest
import allure

@allure.description("Print all titles and proces")
@allure.title("Verify that 62 items are there for macmini")
def test_ebay():
    firefox_options = Options()
    firefox_options.add_argument("--incognito")
    firefox_options.add_argument("--start-maximized")
    driver = webdriver.Firefox(firefox_options)
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")

    search_box_input_path = driver.find_element(By.XPATH,"//input[@placeholder='Search for anything']")
    search_box_input_path.send_keys("macmini")

    search_button = driver.find_element(By.XPATH,"//span[@class='gh-search-button__label']")
    search_button.click()

    # //div[@class="s-item__title"] -> div.s-item__title

    list_of_items = driver.find_elements(By.CSS_SELECTOR, ".s-item__title")
    list_of_items_price = driver.find_elements(By.CSS_SELECTOR, ".s-item__price")
    #
    # for items in list_of_items:
    #     print(items.text)
    #
    # for prices in list_of_items_price:
    #     print(prices.text)

    for items, prices in (zip(list_of_items,list_of_items_price)):
        print(items.text)
        print(prices.text)

    print(len(list_of_items))
    print(len(list_of_items_price))

    driver.quit()

