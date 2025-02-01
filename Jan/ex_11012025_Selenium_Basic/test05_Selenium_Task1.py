from selenium import webdriver
import pytest
import allure

@allure.title("verify the title and current url")
def test_Task1():
    driver = webdriver.Chrome()
    driver.get("https://demo.us.espocrm.com/")
    print(driver.current_url)
    print(driver.title)
    assert driver.current_url == "https://demo.us.espocrm.com/"
    assert driver.title == "EspoCRM Demo"