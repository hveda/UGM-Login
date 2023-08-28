#!/usr/bin/python3
# import os,sys
# import random
# import time
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, NoSuchElementException, WebDriverException  
from config import ugm_username, ugm_password
import logging


logging.basicConfig(filename='app.log', level=logging.INFO)  

try:
    # Using ChromeDriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)

    # Using FirefoxDriver
    # driver = webdriver.Firefox()

    driver.set_window_size(800, 600)
    driver.get('https://internet.ugm.ac.id/sso/login')

    #enter username
    email = driver.find_element_by_id("username")
    email.send_keys(ugm_username)

    #enter password
    password = driver.find_element_by_id("password")
    password.send_keys(ugm_password)
    if not ugm_username:  
        raise ValueError("Username is empty")  
    if not ugm_password:  
        raise ValueError("Password is empty")  

    #login
    loginBtn = driver.find_element_by_name("submit")
    loginBtn.click()

    # using this line for closing chrome driver
    driver.close()
    logging.info("Login successful")  

except NoSuchElementException as e:  
    logging.error("Element not found:", e)  
except WebDriverException as e:  
    logging.error("WebDriver error:", e)  
