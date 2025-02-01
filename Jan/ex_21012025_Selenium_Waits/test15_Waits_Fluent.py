from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
import pytest
import allure

@allure.title("app.vwo.com login page with fluent waits")
@allure.description("Verify that app.vwo.com page is loaded with fluent waits")
def test_app_vwo():
    driver = webdriver.Firefox()
    driver.get("https://app.vwo.com/#/login")

    email_web_element = driver.find_element(By.CSS_SELECTOR,"#login-username")
    email_web_element.send_keys("abc@gmail.com")

    password_web_element = driver.find_element(By.CSS_SELECTOR,"#login-password")
    password_web_element.send_keys("1234")

    submit_button_web_element = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
    submit_button_web_element.click()

    # Wait for the error message

    # A Condition to check the element
    # error_msg_element - comes after 2-4 seconds
    # I have to wait with some condition -
    # wait with the condition
    # Add a condition so that Webdriver should wait for that condition.
    # element is visible then assertion
    # when  this -> then do this

    # Smart Logic to wait for the element
    # Condition based Logic

    # Verify that message is visible.
    # Fluent wait checks fro the element at regular intervals .Memory efficient

    ignore_list = [ElementNotVisibleException, ElementNotInteractableException, ElementNotSelectableException]
    WebDriverWait(driver=driver,poll_frequency=1,timeout=3,ignored_exceptions=ignore_list).until(EC.visibility_of_element_located((By.ID,"js-notification-box-msg")))

    # time.sleep(4) #Here python interpreter is halted for 5 seconds without any condition >less efficient
    error_msg_element = driver.find_element(By.ID,"js-notification-box-msg")
    print(error_msg_element.text)

    assert error_msg_element.text == "Your email, password, IP address or location did not match"

    driver.quit()