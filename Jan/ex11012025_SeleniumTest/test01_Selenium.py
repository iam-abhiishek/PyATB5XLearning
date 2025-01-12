import time

from selenium import webdriver
import pytest
import allure

@allure.title("open facebook homepage")
def test_open_broswer():
    driver = webdriver.Chrome()
    driver.get("https://facebook.com")
    time.sleep(15)
