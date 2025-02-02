import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from allure_commons.types import AttachmentType

@allure.description("Verify action p1")
@allure.title("Action P1")
def test_verify_action_makemytrip():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    # firefox_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    driver.get("https://www.makemytrip.com/")

    WebDriverWait(driver=driver,timeout=5).until(EC.visibility_of_element_located((By.XPATH,"//span[@class='commonModal__close']")))
    close = driver.find_element(By.XPATH,"//span[@class='commonModal__close']")
    close.click()

    from_city = driver.find_element(By.ID,"fromCity")
    actions = ActionChains(driver=driver)
    actions.move_to_element(from_city).click().send_keys("del").perform()

    time.sleep(2)
    actions.move_to_element(from_city).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
    allure.attach(driver.get_screenshot_as_png(), name="login-ss", attachment_type=AttachmentType.PNG)

    time.sleep(5)
    driver.quit()