from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import pytest
import allure

@allure.title("VWO login Page with waits")
@allure.description("TC1-Negative-Verify that VWO login page is loaded with waits")
@pytest.mark.negative
def test_app_vwo():
    driver = webdriver.Firefox()
    driver.get("https://app.vwo.com/#/login")
    driver.implicitly_wait(5)
    email_web_element = driver.find_element(By.CSS_SELECTOR,"#login-username")
    email_web_element.send_keys("abc@gmail.com")

    password_web_element = driver.find_element(By.CSS_SELECTOR,"#login-password")
    password_web_element.send_keys("1234")

    driver.quit()