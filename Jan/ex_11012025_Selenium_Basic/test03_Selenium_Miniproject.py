from selenium import webdriver
import pytest
import allure

def test_miniproject():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "cura Healthcare Service" in driver.page_source:
        print("Text found!!")
    else:
        print("Text not found")
        pytest.fail("Text not found on page")

       # close the browser - Python interpreter is closing