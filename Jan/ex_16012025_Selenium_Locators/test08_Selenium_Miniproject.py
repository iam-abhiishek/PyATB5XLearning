import os
import time

from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

@allure.title("VWO Login Negative Testcase")
@allure.description("TC1 - Negative TC - VWO Login with invalid creds.")
@pytest.mark.negativevwologin
def test_app_vwo_login_chrome():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))

    email_web_element = driver.find_element(By.ID,"login-username")
    email_web_element.send_keys(os.getenv("INVALID_USERNAME"))

    password_web_element = driver.find_element(By.ID,"login-password")
    password_web_element.send_keys(os.getenv("INVALID_PASSWORD"))

    submit_web_element = driver.find_element(By.ID,"js-login-btn")
    submit_web_element.click()

    time.sleep(3)

    error_message_web_element = driver.find_element(By.CLASS_NAME,"notification-box-description")
    print(error_message_web_element.text)

    assert error_message_web_element.text == os.getenv("error_message_expected")

    time.sleep(5)
    driver.quit()




