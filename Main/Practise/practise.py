from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urllib3 import request
from urllib3.connection import HTTPSConnection

Chromium_Options = ChromiumOptions()
Chromium_Options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=Chromium_Options)
driver.implicitly_wait(10)

#enter text
# driver.get("https://the-internet.herokuapp.com/inputs")
# driver.find_element(By.XPATH,"//input[@type='number']").send_keys("123")

# #Handle JS alert
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
# alert = Alert(driver)
# alert.accept()
#
# success=driver.find_element(By.ID,"result").text
# assert success == "You successfully clicked an alert"

# #Broken images
# driver.get("https://the-internet.herokuapp.com/broken_images")
# driver.maximize_window()
# all_images = driver.find_elements(By.TAG_NAME,"img")
# list = []
# for img in all_images:
#     link = img.get_attribute("src")
#     response = requests.get(link, timeout=5)
#     if response.status_code != 200:
#         list.append(link)
#         continue
# print(f"broken links : {list}")

