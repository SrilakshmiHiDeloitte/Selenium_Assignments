from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import pytest


def test_assign2():
    driver = webdriver.Chrome(executable_path='C:\\Users\\visrilakshmi\\Downloads\\chromedriver.exe')
    driver.get('https://webdriveruniversity.com/index.html')
    driver.maximize_window()
    time.sleep(2)
    a = driver.find_elements(by=By.CLASS_NAME, value='section-title')

    for i in a:
        if i.text == 'BUTTON CLICKS':
            i.click()
            time.sleep(2)

    b = driver.window_handles[0]

    def wind():
        c = driver.window_handles
        for w in c:
            if w != b:
                driver.switch_to.window(w)
                break

    wind()
    driver.find_element(by=By.ID, value='button1').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value='//*[@id="myModalClick"]/div/div/div[3]/button').click()
    time.sleep(2)
    driver.find_element(by=By.ID, value='button2').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value='//*[@id="myModalJSClick"]/div/div/div[3]/button').click()
    time.sleep(2)
    driver.find_element(by=By.ID, value='button3').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value='//*[@id="myModalMoveClick"]/div/div/div[3]/button').click()
    time.sleep(2)
    driver.close()
    driver.switch_to.window(b)

    for i in a:
        if i.text == 'TO DO LIST':
            i.click()
    wind()
    # TODO
    time.sleep(2)
    tod = driver.find_element(by=By.XPATH, value='//*[@id="container"]/input')
    time.sleep(2)
    tod.send_keys('Hi...Testing')
    tod.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.close()
    driver.switch_to.window(b)
    for i in a:
        if i.text == 'DROPDOWN, CHECKBOXE(S) & RADIO BUTTON(S)':
            i.click()
            time.sleep(2)
    wind()

    m = driver.find_elements(by=By.CLASS_NAME, value='dropdown-menu-lists')
    for i in m:
        y = Select(i)
        y.select_by_index(1)
        time.sleep(2)

    # checkbox
    driver.find_element(by=By.XPATH, value='//*[@id="checkboxes"]/label[1]/input').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value='//*[@id="checkboxes"]/label[2]/input').click()
    time.sleep(2)
    m = driver.find_elements(by=By.CLASS_NAME, value='radio-buttons')
    for i in m:
        if i.text == 'Yellow':
            i.click()
            time.sleep(2)
            break
    driver.close()
    time.sleep(3)

    # Scrolling Around
    driver.switch_to.window(b)
    for i in a:
        if i.text == 'SCROLLING AROUND':
            i.click()
            time.sleep(2)
    wind()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.close()
    driver.switch_to.window(b)
    # Autocomplete Text Fields
    for i in a:
        if i.text == 'AUTOCOMPLETE TEXTFIELD':
            i.click()
            time.sleep(2)
    wind()
    driver.find_element(by=By.ID, value='myInput').send_keys('Burger')
    time.sleep(2)
    driver.find_element(by=By.ID, value='submit-button').click()
    time.sleep(2)
    driver.close()
    driver.switch_to.window(b)
    time.sleep(3)

    for i in a:
        if i.text == 'FILE UPLOAD':
            i.click()
            time.sleep(2)
    wind()
    driver.find_element(by=By.ID, value='myFile').send_keys('C:\\Users\\visrilakshmi\\Downloads\\pexels-photo-2486168'
                                                            '.jpeg')
    time.sleep(2)
    driver.find_element(by=By.ID, value='submit-button').click()
    time.sleep(2)
    alert = Alert(driver)
    alert.accept()









