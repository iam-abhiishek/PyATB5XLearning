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

    all_link_page = driver.find_elements(By.TAG_NAME, "a")
    print(len(all_link_page))
    for i in all_link_page:
        print(i.text)
        if "Start a free trial" in i.text:
            i.click()


    time.sleep(5)
    driver.quit()




