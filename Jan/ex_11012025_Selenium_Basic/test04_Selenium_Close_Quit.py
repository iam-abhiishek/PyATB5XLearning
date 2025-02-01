import time

from selenium import webdriver
import pytest
import allure

def test_katalon_chrome():
    driver = webdriver.Firefox()
    driver.get("https://www.facebook.com")
    assert driver.current_url == "https://www.facebook.com/"
    time.sleep(10)
    #driver.close()  # close current window
    driver.quit()    # close everything
