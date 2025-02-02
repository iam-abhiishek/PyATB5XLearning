import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import pytest
import allure

def test_spicejet():
    chrome_options = Options()
    driver = webdriver.Chrome(chrome_options)
    chrome_options.add_argument("--incognito")
    driver.maximize_window()
    driver.get("https://www.spicejet.com/")

    prefs = {
        "profile.default_content_setting_values.notifications": 1  # 1 allows, 2 blocks
    }
    chrome_options.add_experimental_option("prefs", prefs)

    from_city = driver.find_element(By.XPATH,"//div[@data-testid='to-testID-origin']//input[@type='text']")
    actions = ActionChains(driver=driver)
    actions.move_to_element(from_city).click().send_keys("mum").perform()

    WebDriverWait(driver=driver,timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//div[@data-testid='to-testID-destination']//div[@class='css-1dbjc4n r-14lw9ot r-11u4nky r-z2wwpe r-1phboty r-rs99b7 r-1loqt21 r-13awgt0 r-ymttw5 r-tju18j r-5njf8e r-1otgn73']")))
    to_city = driver.find_element(By.XPATH,"//div[@data-testid='to-testID-destination']//div[@class='css-1dbjc4n r-14lw9ot r-11u4nky r-z2wwpe r-1phboty r-rs99b7 r-1loqt21 r-13awgt0 r-ymttw5 r-tju18j r-5njf8e r-1otgn73']")
    actions.move_to_element(to_city).click().send_keys("blr").perform()

    ignore_list = (ElementNotVisibleException, ElementNotInteractableException, ElementNotSelectableException)
    WebDriverWait(driver=driver, poll_frequency=1, timeout=10, ignored_exceptions=ignore_list).until(
        EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[7]/div[2]/div[1]")))
    search_element = driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[7]/div[2]/div[1]")

    search_element.click()

    time.sleep(5)