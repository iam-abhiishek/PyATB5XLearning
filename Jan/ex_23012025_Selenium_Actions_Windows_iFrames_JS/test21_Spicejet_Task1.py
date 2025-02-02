import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure

def test_spicejet():
    chrome_options = Options()
    driver = webdriver.Chrome(chrome_options)
    # chrome_options.add_argument("--incognito")
    driver.maximize_window()
    driver.get("https://www.spicejet.com/")

    WebDriverWait(driver=driver,timeout=3).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    # WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())
    # alert = driver.switch_to.alert
    alert.dismiss()

    time.sleep(3)