from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome('C:\\Users\\visrilakshmi\\Downloads\\chromedriver.exe')
driver.get('https://www.goibibo.com/')
driver.implicitly_wait(5)
# goibibo logo
# absolute xpath
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[1]/div/header/a/span')

# login
# using id
driver.find_element(by=By.ID, value='get_sign_in')

# flights
# by css selector
driver.find_element(by=By.CSS_SELECTOR,
                    value='#root > div > div.xayxd-0.hdrtUp > div > header > ul > li.active.\. > a > span')

#Hotels
# absolute xpath
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[1]/div/header/ul/li[2]/a/span')


#From
# using absolute xpath
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/p')

# Search
# using css selector
driver.find_element(by=By.CSS_SELECTOR,
                    value='#root > div > div.header__conts > div.header__contInners > div > div.sc-ctqQKy.cYIhJv > span')


# Student Fare
# absolute xpath
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div[1]/div/ul/li[4]')

#products
# absolute xpath
driver.find_element(by=By.XPATH, value='//*[@id="productAnchor"]/div[3]/div/div[2]/a')

#Round Trip
# using absolute xpath
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div[1]/div/ul/li[1]')



