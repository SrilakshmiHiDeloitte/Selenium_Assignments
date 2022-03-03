import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Selenium_Assignments.Main_Assignment_Flipkart.Test_Data import Test_Data

logging.basicConfig(filename='shopping.log', level=logging.DEBUG)

driver = webdriver.Chrome(executable_path=Test_Data.chrome_path)
driver.get(Test_Data.url)
time.sleep(3)
driver.maximize_window()
time.sleep(3)

"""Test case1 - log in into application and opening grocery"""


def test_do_login():
    driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input').send_keys(
        Test_Data.email)
    time.sleep(3)
    driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input').send_keys(
        Test_Data.pswd)
    time.sleep(3)
    driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button').click()
    time.sleep(3)
    a = driver.find_elements(by=By.XPATH, value='//div[@class="xtXmba"]')
    for i in a:
        if i.text == 'Grocery':
            i.click()
    # ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "pincode")))
    time.sleep(2)
    driver.find_element(by=By.NAME, value='pincode"]').send_keys(Test_Data.pin)
    time.sleep(2)
    driver.find_element(by=By.NAME, value='pincode"]').send_keys(Keys.ENTER)
    time.sleep(2)


"""Test case 2 - adding 3 items to cart and verify the cart if they were added or not"""


def test_grocery_adding_item1():
    # adding item from Tea
    time.sleep(4)
    a = ActionChains(driver)
    a.move_to_element(driver.find_element(By.XPATH, "//*[@alt='Snacks & Beverages']")).perform()
    time.sleep(7)
    a.move_to_element(driver.find_element(By.LINK_TEXT, "Tea")).perform()
    time.sleep(7)
    driver.find_element(By.LINK_TEXT, 'Tea').click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > .\_2OvUl0 .\_3BhXPZ:nth-child(4) span').click()
    time.sleep(4)
    driver.back()


def test_grocery_adding_item2():
    # adding item from Packaged foods
    time.sleep(7)
    a = ActionChains(driver)
    a.move_to_element(driver.find_element(By.XPATH, "//*[@alt='Packaged Food']")).perform()
    time.sleep(7)
    a.move_to_element(driver.find_element(By.LINK_TEXT, "Chocolates & Sweets")).perform()
    time.sleep(7)
    driver.find_element(By.LINK_TEXT, 'Chocolates').click()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > .\_2OvUl0 .\_3BhXPZ:nth-child(4) span').click()
    time.sleep(4)
    driver.back()


def test_adding_item3():
    # adding item from Home and Kitchen
    time.sleep(7)
    a = ActionChains(driver)
    a.move_to_element(driver.find_element(By.XPATH, "//*[@alt='Household Care']")).perform()
    time.sleep(7)
    a.move_to_element(driver.find_element(By.LINK_TEXT, "Detergents & Laundry")).perform()
    time.sleep(7)
    driver.find_element(By.LINK_TEXT, 'Detergents').click()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > .\_2OvUl0 .\_3BhXPZ:nth-child(4) span').click()
    time.sleep(4)
    driver.back()


# verifying the cart
def test_verify_cart():
    driver.find_element(by=By.XPATH, value='//div//a[@class="_3SkBxJ"]').click()
    time.sleep(2)
    item_count = driver.find_element(by=By.XPATH, value='//div[@class="_3g_HeN"]').text
    for i in item_count:
        if i.isdigit():
            items_cart = i
    print(items_cart)
    assert items_cart == 3, 'More than 3 items are added'
    time.sleep(4)


"""test case 3 - Searching and filtering the items with 'Besan' as keyword """


def test_search_filter():
    driver.find_element(By.CSS_SELECTOR, '.\_2xm1JU').click()
    time.sleep(4)
    a = driver.find_elements(by=By.XPATH, value='//div[@class="xtXmba"]')
    for i in a:
        if i.text == 'Grocery':
            i.click()
    # ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "pincode")))
    time.sleep(6)
    driver.find_element(by=By.XPATH, value='//input[@class="_3704LK"]').send_keys(Test_Data.search_item)
    time.sleep(2)
    driver.find_element(by=By.XPATH, value='//button[@class="L0Z3Pu"]').click()
    time.sleep(2)
    brand_select = driver.find_element(by=By.XPATH,
                                       value='//*[@id="container"]/div/div[3]/div[2]/div[1]/div/div/section[2]/div[2]/div/div[4]/div/label')
    brand_select.click()
    brand = brand_select.text.split(' ')
    print(brand)
    brand_data = driver.find_elements(by=By.CLASS_NAME, value='_2gX9pM')
    brand_list = []
    for i in brand_data:
        brand_list.append(i.text)
    assert brand[0] in brand_list[0], 'Filtered data is not showing'


""" test case 4 - Adding 2 random fashion items to wishlist and verifying if they are added or not """


def test_fashion_wishlist():
    time.sleep(7)
    driver.find_element(By.CSS_SELECTOR, '.\_1fqNI-').click()
    time.sleep(4)
    a = ActionChains(driver)
    a.move_to_element(driver.find_element(By.XPATH, "//*[@alt='Fashion']")).perform()
    time.sleep(7)
    a.move_to_element(driver.find_element(By.LINK_TEXT, "Women Ethnic")).perform()
    time.sleep(7)
    driver.find_element(By.LINK_TEXT, "Women Sarees").click()
    time.sleep(4)
    driver.find_element(By.XPATH,
                        '//*[@id="container"]/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/a/div[1]').click()
    time.sleep(4)
    fashion_list = driver.find_elements(by=By.XPATH, value='//div[@class="_2hVSre _1DmLJ5 -o7Q4n"]')
    time.sleep(3)
    j = 1
    for i in fashion_list:
        if j <= 2:
            i.click()
            # driver.find_element(by=By.XPATH, value='//div[@class="_2hVSre _1DmLJ5 -o7Q4n"]').click()
            j = j + 1
    # Verifying wishlist
    a = ActionChains(driver)
    a.move_to_element(driver.find_element(By.CSS_SELECTOR, ".go_DOp:nth-child(3) .exehdJ")).perform()
    time.sleep(6)
    driver.find_element(By.CSS_SELECTOR, '.\_2NOVgj:nth-child(5) > .\_2kxeIr').click()
    time.sleep(6)
    wish_list_count = driver.find_element(By.CSS_SELECTOR, '.\_3FVYY1 > span').text
    print(wish_list_count)
    wish_listed = ''
    for i in wish_list_count:
        if i.isdigit():
            wish_listed = wish_listed + str(i)
    assert wish_listed == 2, 'More than 2 items are added'


""" Test case 5 - Adding new address to the profile"""


def test_add_new_address():
    a = ActionChains(driver)
    # account name
    a.move_to_element(driver.find_element(By.CSS_SELECTOR, ".go_DOp:nth-child(3) .exehdJ")).perform()
    time.sleep(4)
    driver.find_element(by=By.CSS_SELECTOR, value='.\_2NOVgj:nth-child(1) .\_3vhnxf').click()
    time.sleep(3)
    driver.find_element(by=By.LINK_TEXT, value='Manage Addresses').click()
    time.sleep(4)
    driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div[2]/div/div/div/button').click()
    time.sleep(4)

    # adding address

    driver.find_element(by=By.NAME, value='name').send_keys(Test_Data.name)
    time.sleep(2)
    driver.find_element(by=By.NAME, value='phone').send_keys(Test_Data.phn)
    time.sleep(2)
    driver.find_element(by=By.NAME, value='pincode').send_keys(Test_Data.pin)
    time.sleep(2)
    driver.find_element(by=By.NAME, value='addressLine2').send_keys(Test_Data.city)
    time.sleep(2)
    driver.find_element(by=By.NAME, value='addressLine1').send_keys(Test_Data.address)
    time.sleep(2)
    driver.find_element(By.NAME, 'landmark').send_keys(Test_Data.land_mark)
    time.sleep(2)
    driver.find_element(By.NAME, 'alternatePhone').send_keys(Test_Data.alt_phn)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.\_2Fn-Ln:nth-child(1)').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.\_1JDhFS').click()
    time.sleep(2)


"""Test case 6 - Logout functionality - Logging out from the application and verifying whether it got logged out or 
not """


def test_logout():
    a = ActionChains(driver)
    # account name
    a.move_to_element(driver.find_element(By.CSS_SELECTOR, ".go_DOp:nth-child(3) .exehdJ")).perform()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, '.\_2NOVgj:nth-child(10) .\_3vhnxf').click()
    time.sleep(4)
    checking = driver.find_element(By.CSS_SELECTOR, '.\_36KMOx > span').text
    assert checking == 'Login', 'Not logged out of application'
