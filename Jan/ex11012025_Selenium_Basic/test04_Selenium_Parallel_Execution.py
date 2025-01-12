from selenium import webdriver
import pytest
import allure

def test_katalon_chrome():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    assert driver.current_url == "https://www.facebook.com/"

def test_katalon_firefox():
    driver = webdriver.Firefox()
    driver.get("https://www.facebook.com")
    assert driver.current_url == "https://www.facebook.com/"