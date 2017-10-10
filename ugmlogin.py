#!/usr/bin/python3
# import os,sys
# import random
# import time
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from config import ugm_username, ugm_password

# ugm_username = "ugm_id"
# ugm_password = "ugm_password"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-notifications')

driver = webdriver.Chrome(chrome_options=chrome_options)

driver.set_window_size(1280, 1000)
driver.get('https://internet.ugm.ac.id/sso/login')

#enter username
email = driver.find_element_by_id("username")
email.send_keys(ugm_username)

#enter password
password = driver.find_element_by_id("password")
password.send_keys(ugm_password)

#login
loginBtn = driver.find_element_by_name("submit")
loginBtn.click()

# using this line for closing chrome driver
driver.close()