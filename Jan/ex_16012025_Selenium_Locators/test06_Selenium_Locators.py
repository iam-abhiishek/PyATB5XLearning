import time

from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By


def test_katalon_chrome():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # 1- Find the element the anchor tag
    # <a
    # id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">
    # Make Appointment
    # </a>

    make_appointment_element = driver.find_element(By.ID,"btn-make-appointment")

    #Click on it
    make_appointment_element.click()

    #Verify URL changes
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(5)
    driver.quit()  # close everything
