import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import allure

@allure.title("JS Alerts")
@allure.description("Verify the 3 types of JS  alerts ")
def test_js_normal_alert():
    driver = webdriver.Firefox()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_js_alert = driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
    element_js_alert.click()

    time.sleep(2)

    WebDriverWait(driver=driver,timeout=3).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    alert_click_text = driver.find_element(By.ID,"result").text
    assert alert_click_text == "You successfully clicked an alert"

    time.sleep(3)
    driver.quit()

def test_alert_js_confirm():
    driver = webdriver.Firefox()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_js_confirm = driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']")
    element_js_confirm.click()

    WebDriverWait(driver=driver,timeout=3).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.dismiss()

    alert_dismiss_text = driver.find_element(By.ID,"result").text
    assert alert_dismiss_text == "You clicked: Cancel"

    time.sleep(3)
    driver.quit()

def test_alerts_prompt():
    driver=webdriver.Firefox()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    element_js_prompt_alert=driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
    element_js_prompt_alert.click()
    WebDriverWait(driver=driver,timeout=3).until(EC.alert_is_present())
    alert=driver.switch_to.alert
    alert.send_keys("Success")
    alert.accept()
    alert_prompt_text=driver.find_element(By.ID,"result").text
    assert alert_prompt_text=="You entered: Success"
    time.sleep(3)
    driver.quit()