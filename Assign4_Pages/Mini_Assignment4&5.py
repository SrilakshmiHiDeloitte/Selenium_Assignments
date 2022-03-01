import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from Selenium_Assignments.Assign4_Pages.Locators import Locators

logging.basicConfig(filename='../../Pages/shopping.log', level=logging.DEBUG)

driver = webdriver.Chrome(executable_path='C:\\Users\\visrilakshmi\\Downloads\\chromedriver.exe')

driver.get('https://weathershopper.pythonanywhere.com/')

driver.maximize_window()
time.sleep(2)
driver.maximize_window()
# items = driver.find_elements(by=By.XPATH, value='//button[@class="btn btn-primary"]')


k = driver.find_element(by=By.ID, value=Locators.temp).text
k = k.split(' ')
temp = int(k[0])


# Adding items to cart based on the info
def adding_items(item):
    rate = []
    for i in items:
        time.sleep(2)
        k = i.text.split('\n')
        z = k[1].split(' ')
        for i in z:
            if i.isdigit():
                m = i
        for j in k:
            if item in j:
                rate.append(m)
    rate = min(rate)
    time.sleep(3)

    for i in items:
        if rate in i.text:
            i.find_element(by=By.XPATH, value=Locators.Add_btn).click()


def payment():
    time.sleep(2)
    driver.find_element(by=By.ID, value=Locators.cart_btn).click()
    time.sleep(3)
    driver.find_element(by=By.CLASS_NAME, value=Locators.pay_btn).click()
    time.sleep(3)

    # Entering Payment Details
    driver.switch_to.frame(Locators.frame)
    driver.find_element(by=By.ID, value=Locators.mail).send_keys(Locators.mail_in)
    time.sleep(2)
    driver.find_element(by=By.ID, value=Locators.card).send_keys(Locators.card_in)
    time.sleep(2)
    driver.find_element(by=By.ID, value=Locators.card).send_keys(Locators.card_in)
    time.sleep(2)
    driver.find_element(by=By.ID, value=Locators.card).send_keys(Locators.card_in)
    time.sleep(2)
    driver.find_element(by=By.ID, value=Locators.card).send_keys(Locators.card_in)
    time.sleep(2)
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
    driver.find_element(by=By.LINK_TEXT, value=Locators.buy_moist).click()
    items = driver.find_elements(by=By.XPATH, value=Locators.items_list)
    adding_items(Locators.moist_item1)
    adding_items(Locators.moist_item2)
    payment()


elif temp >= 34:
    driver.find_element(by=By.LINK_TEXT, value=Locators.buy_sunsc).click()
    items = driver.find_elements(by=By.XPATH, value=Locators.items_list)
    adding_items(Locators.sunscr_item1)
    adding_items(Locators.sunscr_item2)
    payment()

