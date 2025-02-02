import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

@allure.description("Verify action p1")
@allure.title("Action P1")
def test_verify_action_keyboard():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/practice.html")
    first_name = driver.find_element(By.XPATH,"//input[@name='firstname']")

    actions = ActionChains(driver=driver)
    (actions
     .key_down(Keys.SHIFT)
     .send_keys_to_element(first_name,"hello how")
     .key_up(Keys.SHIFT)
     .perform())

    time.sleep(5)
    driver.quit()