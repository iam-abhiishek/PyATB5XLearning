import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import allure

@allure.title("Modals")
@allure.description("Verify Modals in Makemy trip site ")
def test_modal_chrome():
    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()
    WebDriverWait(driver=driver,timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//span[@class='commonModal__close']")))

    modal = driver.find_element(By.XPATH,"//span[@class='commonModal__close']")
    modal.click()
    time.sleep(3)
