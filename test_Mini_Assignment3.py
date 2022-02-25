import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import pytest


def test_mini_assign3():
    driver = webdriver.Chrome(executable_path='C:\\Users\\visrilakshmi\\Downloads\\chromedriver.exe')
    driver.get('https://the-internet.herokuapp.com/')
    driver.implicitly_wait(5)
    driver.maximize_window()
    time.sleep(5)
    # Double click
    driver.find_element(by=By.LINK_TEXT, value='JavaScript Alerts').click()
    time.sleep(5)
    driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/ul/li[1]/button').click()
    time.sleep(5)
    alert = Alert(driver)
    alert.accept()
    driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/ul/li[2]/button').click()
    time.sleep(5)
    alert = Alert(driver)
    c = alert.text
    alert.accept()
    print(c)
    driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/ul/li[3]/button').click()
    time.sleep(5)
    alert = Alert(driver)
    alert.send_keys(c)
    alert.accept()
