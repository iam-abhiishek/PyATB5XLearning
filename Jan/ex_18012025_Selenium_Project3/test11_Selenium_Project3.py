import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest
import allure
from dotenv import load_dotenv

@allure.title("Verify account registration is completed")
@allure.description("TC1: Registration completion")
@pytest.mark.positive
def test_account_registration():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    first_name_web_element = driver.find_element(By.ID,"input-firstname")
    first_name_web_element.send_keys("Abhishek")

    last_name_web_element = driver.find_element(By.ID, "input-lastname")
    last_name_web_element.send_keys("Kumar")

    email_web_element = driver.find_element(By.ID,"input-email")
    email_web_element.send_keys("abhiluck999@gmail.com")

    telephone_web_element = driver.find_element(By.ID,"input-telephone")
    telephone_web_element.send_keys("7089772866")

    password_web_element = driver.find_element(By.ID,"input-password")
    password_web_element.send_keys("Pass1234")

    confirm_pass_web_element = driver.find_element(By.ID,"input-confirm")
    confirm_pass_web_element.send_keys("Pass1234")

    radio_web_element = driver.find_element(By.XPATH,"//input[@value='0']")
    radio_web_element.click()

    agree_web_element = driver.find_element(By.NAME,"agree")
    agree_web_element.click()

    time.sleep(3)

    continue_web_element = driver.find_element(By.XPATH,"//input[@value='Continue']")
    continue_web_element.click()

    time.sleep(5)
    # driver.quit()



