import time
import os
from selenium import webdriver
import pyautogui
import time
import os

path = os.getcwd()
DRIVER = 'chromedriver'
driver = webdriver.Chrome(DRIVER)
driver.maximize_window()
driver.get('https://www.findaya.com/')
time.sleep(10)
pyautogui.screenshot('image.jpg')