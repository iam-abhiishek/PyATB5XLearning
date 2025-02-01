from selenium import webdriver
import pytest
import allure

@allure.title("Verify that the title of vwo.com is expected")
def test_vwo_sample():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"
    print(driver.page_source)
    print(driver.current_url)