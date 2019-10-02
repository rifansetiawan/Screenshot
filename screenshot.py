import time
import os
from selenium import webdriver
import pyautogui
import os

path = os.getcwd()
DRIVER = 'chromedriver'

chrome_options = webdriver.ChromeOptions()
if os.name == "nt":
    # If current OS is Windows
    chrome_options.add_argument("--start-maximized")
else:
    # Other OS (Mac / Linux)
    chrome_options.add_argument("--kiosk")

driver = webdriver.Chrome(DRIVER, chrome_options = chrome_options)
driver.get('https://www.findaya.com/')
time.sleep(10)
pyautogui.screenshot('image.jpg')