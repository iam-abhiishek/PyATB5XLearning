import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest
import allure

def test_window_handles():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/windows")

    parent_window = driver.current_window_handle
    print(parent_window)

    click_element = driver.find_element(By.XPATH,"//a[normalize-space()='Click Here']")
    click_element.click()

    window_handles = driver.window_handles
    print(window_handles)

    for handle in window_handles:
        driver.switch_to.window(handle)
        if "New Window" in driver.page_source:
            print("tc passed")
            break

    time.sleep(5)

