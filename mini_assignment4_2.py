import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest
from selenium.webdriver.common.alert import Alert
from Pages.Basepage import BasePage
from Pages.Locators import Locators

driver = webdriver.Chrome(executable_path='C:\\Users\\visrilakshmi\\Downloads\\chromedriver.exe')

driver.get('https://weathershopper.pythonanywhere.com/')
time.sleep(2)
driver.maximize_window()
items = driver.find_elements(by=By.XPATH, value='//button[@class="btn btn-primary"]')

k = driver.find_element(by=By.ID, value='temperature').text
k = k.split(' ')
temp = int(k[0])


# Adding items to cart
if temp <= 19:
    driver.find_element(by=By.LINK_TEXT, value='Buy moisturizers').click()
    time.sleep(3)
    rate = []
    for i in items:
        time.sleep(2)
        k = i.text.split('\n')
        print(k)
        z = k[1].split(' ')
        for i in z:
            if i.isdigit():
                m = i
        print(m)
        for j in k:
            if 'Aloe' in j:
                rate.append(m)
    rate = min(rate)
    print(rate)
    time.sleep(3)

    for i in items:
        if rate in i.text:
            i.find_element(by=By.XPATH, value='//button[@class="btn btn-primary"]').click()

    # Second Item
    rate = []
    for i in items:
        k = i.text.split('\n')
        print(k)
        z = k[1].split(' ')
        for i in z:
            if i.isdigit():
                m = i
        print(m)
        for j in k:
            if 'Almond' in j:
                rate.append(m)
    rate = min(rate)
    print(rate)
    time.sleep(3)

    for i in items:
        if rate in i.text:
            i.find_element(by=By.XPATH, value='//button[@class="btn btn-primary"]').click()

    driver.find_element(by=By.ID, value='cart').click()
    time.sleep(3)
    driver.find_element(by=By.CLASS_NAME, value='stripe-button-el').click()
    time.sleep(3)

    # Entering Payment Details
    driver.switch_to.frame('stripe_checkout_app')
    driver.find_element(by=By.ID, value='email').send_keys('sri@gmail.com')
    time.sleep(3)
    driver.find_element(by=By.ID, value='card_number').send_keys('4242')
    time.sleep(3)
    driver.find_element(by=By.ID, value='card_number').send_keys('4242')
    driver.find_element(by=By.ID, value='card_number').send_keys('4242')
    driver.find_element(by=By.ID, value='card_number').send_keys('4242')
    time.sleep(3)
    driver.find_element(by=By.ID, value='cc-exp').send_keys('02')
    time.sleep(3)
    driver.find_element(by=By.ID, value='cc-exp').send_keys('23')
    time.sleep(3)
    driver.find_element(by=By.ID, value='cc-csc').send_keys('471')
    time.sleep(3)
    driver.find_element(by=By.ID, value='billing-zip').send_keys('533125')
    time.sleep(3)
    driver.find_element(by=By.ID, value='submitButton').click()


elif temp >= 34:
    driver.find_element(by=By.LINK_TEXT, value='Buy sunscreens').click()
    # adding_items('SPF-50', 'SPF-30')
    driver.find_element(by=By.LINK_TEXT, value='Buy moisturizers').click()
    time.sleep(3)
    rate = []
    for i in items:
        time.sleep(2)
        k = i.text.split('\n')
        print(k)
        z = k[1].split(' ')
        for i in z:
            if i.isdigit():
                m = i
        print(m)
        for j in k:
            if 'SPF-50' in j:
                rate.append(m)
    rate = min(rate)
    print(rate)
    time.sleep(3)

    for i in items:
        if rate in i.text:
            i.find_element(by=By.XPATH, value='//button[@class="btn btn-primary"]').click()

    # Second Item
    rate = []
    for i in items:
        k = i.text.split('\n')
        print(k)
        z = k[1].split(' ')
        for i in z:
            if i.isdigit():
                m = i
        print(m)
        for j in k:
            if 'SPF-30' in j:
                rate.append(m)
    rate = min(rate)
    print(rate)
    time.sleep(3)

    for i in items:
        if rate in i.text:
            i.find_element(by=By.XPATH, value='//button[@class="btn btn-primary"]').click()

    driver.find_element(by=By.ID, value='cart').click()
    time.sleep(3)
    driver.find_element(by=By.CLASS_NAME, value='stripe-button-el').click()
    time.sleep(3)

    # Entering Payment Details
    driver.switch_to.frame('stripe_checkout_app')
    driver.find_element(by=By.ID, value='email').send_keys('sri@gmail.com')
    time.sleep(3)
    driver.find_element(by=By.ID, value='card_number').send_keys('4242')
    time.sleep(3)
    driver.find_element(by=By.ID, value='card_number').send_keys('4242')
    driver.find_element(by=By.ID, value='card_number').send_keys('4242')
    driver.find_element(by=By.ID, value='card_number').send_keys('4242')
    time.sleep(3)
    driver.find_element(by=By.ID, value='cc-exp').send_keys('02')
    time.sleep(3)
    driver.find_element(by=By.ID, value='cc-exp').send_keys('23')
    time.sleep(3)
    driver.find_element(by=By.ID, value='cc-csc').send_keys('471')
    time.sleep(3)
    driver.find_element(by=By.ID, value='billing-zip').send_keys('533125')
    time.sleep(3)
    driver.find_element(by=By.ID, value='submitButton').click()
