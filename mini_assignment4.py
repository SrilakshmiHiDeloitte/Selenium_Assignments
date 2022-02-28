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
items = driver.find_elements(by=By.XPATH, value=Locators.items_list)

k = driver.find_element(by=By.ID, value=Locators.temp).text
k = k.split(' ')
temp = int(k[0])


def adding_items(item1, item2):
    rate = []
    for i in items:
        h = i.text.split('\n')
        print(k)
        z = h[1].split(' ')
        for i in z:
            if i.isdigit():
                m = i
        print(m)
        for j in h:
            if item1 in j:
                rate.append(m)
    rate = min(rate)
    print(rate)
    time.sleep(3)

    for i in items:
        if rate in i.text:
            i.find_element(by=By.XPATH, value=Locators.items_list).click()

    # Second Item
    rate = []
    for i in items:
        k_item = i.text.split('\n')
        print(k_item)
        z = k_item[1].split(' ')
        for i in z:
            if i.isdigit() == True:
                m = i
        print(m)
        for j in k_item:
            if item2 in j:
                rate.append(m)
    rate = min(rate)
    print(rate)
    time.sleep(3)

    for i in items:
        if rate in i.text:
            i.find_element(by=By.XPATH, value=Locators.Add_btn).click()

    driver.find_element(by=By.ID, value=Locators.cart_btn).click()
    time.sleep(3)
    driver.find_element(by=By.CLASS_NAME, value=Locators.pay_btn).click()
    time.sleep(3)

    # Entering Payment Details
    driver.switch_to.frame(Locators.frame)
    driver.find_element(by=By.ID, value=Locators.mail).send_keys(Locators.mail_in)
    time.sleep(3)
    driver.find_element(by=By.ID, value=Locators.card).send_keys(Locators.card_in)
    time.sleep(3)
    driver.find_element(by=By.ID, value=Locators.card).send_keys(Locators.card_in)
    driver.find_element(by=By.ID, value=Locators.card).send_keys(Locators.card_in)
    driver.find_element(by=By.ID, value=Locators.card).send_keys(Locators.card_in)
    time.sleep(3)
    driver.find_element(by=By.ID, value=Locators.card_date).send_keys(Locators.card_date_in1)
    time.sleep(3)
    driver.find_element(by=By.ID, value=Locators.card_date).send_keys(Locators.card_date_in2)
    time.sleep(3)
    driver.find_element(by=By.ID, value=Locators.card_cvv).send_keys(Locators.card_cvv_in)
    time.sleep(3)
    driver.find_element(by=By.ID, value=Locators.pincode).send_keys(Locators.pin_in)
    time.sleep(3)
    driver.find_element(by=By.ID, value=Locators.sub_pay).click()


if temp <= 19:
    driver.find_element(by=By.LINK_TEXT, value='Buy moisturizers').click()
    adding_items(Locators.moist_item1, Locators.moist_item2)
elif temp >= 34:
    driver.find_element(by=By.LINK_TEXT, value='Buy sunscreens').click()
    adding_items(Locators.moist_item1, Locators.moist_item2)
