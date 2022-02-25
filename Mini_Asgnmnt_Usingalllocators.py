from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('C:\\Users\\visrilakshmi\\Downloads\\chromedriver.exe')
driver.get('https://www.goibibo.com/')
# goibibo logo

# relative xpath
driver.find_element(by=By.XPATH,value='//a[@class="gi-header-logo__home"]')
# absolute xpath
driver.find_element(by=By.XPATH,value='//*[@id="root"]/div/div[1]/div/header/a/span')
# using class
driver.find_element(by=By.CLASS_NAME,value='header-sprite logo')
# using css selector
driver.find_element(by=By.CSS_SELECTOR,value='#root > div > div.xayxd-0.hdrtUp > div > header > a > span')


# login
# using relative xpath
driver.find_element(by=By.XPATH,value='//div//p[@class="gr-cap-text gr-blue-text gr-bold"]')
#using absolute xpath
driver.find_element(by=By.XPATH,value='//*[@id="root"]/div/div[1]/div/header/div[2]/div/span')
# using tag name
driver.find_element(by=By.TAG_NAME,value='Login or Signup')
# using id
driver.find_element(by=By.ID,value='get_sign_in')
# using css selector
driver.find_element(by=By.CSS_SELECTOR,value='#get_sign_in')

# Flights
# relative xpath
driver.find_element(by=By.XPATH,value='//a[@class="nav-link active"]')
# absolute xpath
driver.find_element(by=By.XPATH,value='//*[@id="root"]/div/div[1]/div/header/ul/li[1]/a')
# by name
driver.find_element(by=By.NAME,value='Flights')
# by css selector
driver.find_element(by=By.CSS_SELECTOR,value='#root > div > div.xayxd-0.hdrtUp > div > header > ul > li.active.\. > a > span')

# Hotels
# relative xpath
driver.find_element(by=By.XPATH,value='//a//span[@class="header-sprite nav-icon-hotels gr-append-right5"]')
# absolute xpath
driver.find_element(by=By.XPATH,value='//*[@id="root"]/div/div[1]/div/header/ul/li[2]/a/span')
# by name
driver.find_element(by=By.NAME,value='Hotels')
# by css selector
driver.find_element(by=By.CSS_SELECTOR,value='#root > div > div.xayxd-0.hdrtUp > div > header > ul > li:nth-child(2) > a > span')


# From
# using relative xpath
driver.find_element(by=By.XPATH,value='//div[@class="sc-bYoBSM jmHUba"]')
# using absolute xpath
driver.find_element(by=By.XPATH,value='//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div[1]/div')
# using tag name
driver.find_element(by=By.TAG_NAME,value='Enter city or airport')
# using css selector
driver.find_element(by=By.CSS_SELECTOR,value='#root > div > div.header__conts > div.header__contInners > div > div.sc-egiyK.hhbEKs > div:nth-child(1) > div')

# Search

# using relative xpath
driver.find_element(by=By.XPATH,value='//div//span[@class="sc-dFtzxp hwZghA"]')
# using absolute xpath
driver.find_element(by=By.XPATH,value='//*[@id="root"]/div/div[2]/div[2]/div/div[3]/span')
# using css selector
driver.find_element(by=By.CSS_SELECTOR,value='#root > div > div.header__conts > div.header__contInners > div > div.sc-ctqQKy.cYIhJv > span')

#Student Fare
# relative xpath
driver.find_element(by=By.XPATH,value='//li[@class="sc-bdvvtL goIptw"]')
# absolute xpath
driver.find_element(by=By.XPATH,value='//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div[1]/div/ul/li[4]')
# using class
driver.find_element(by=By.CLASS_NAME,value='sc-bdvvtL goIptw')
# using css selector
driver.find_element(by=By.CSS_SELECTOR,value='#root > div > div.header__conts > div.header__contInners > div > div.sc-llYSUQ.dGuBYI > div.sc-iJKOTD.eXAvNb > div > ul > li:nth-child(4)')


# Products

# relative xpath
driver.find_element(by=By.XPATH,value='//div//a[@class="fb button orange padLR30 txtTransUpper marginB10 fltHpySrchBtn"]')
# absolute xpath
driver.find_element(by=By.XPATH,value='//*[@id="productAnchor"]/div[3]/div/div[2]/a')
# using class
driver.find_element(by=By.CLASS_NAME,value='fb button orange padLR30 txtTransUpper marginB10 fltHpySrchBtn')
# using tag name
driver.find_element(by=By.TAG_NAME,value='VIEW ALL PRODUCTS')
# using css selector
driver.find_element(by=By.CSS_SELECTOR,value='#productAnchor > div.padTB20 > div > div.txtCenter.flexCol.alignItemsCenter > a')


# Round Trip

# relative xpath
driver.find_element(by=By.XPATH,value='//li[@class="sc-cZMNgc dCkKyZ"]')
# absolute xpath
driver.find_element(by=By.XPATH,value='//*[@id="root"]/div/div[2]/div[2]/div/ul/li[2]')
# using class
driver.find_element(by=By.CLASS_NAME,value='sc-cZMNgc dCkKyZ')
# using name
driver.find_element(by=By.NAME,value='Round-trip')
# using css selector
driver.find_element(by=By.CSS_SELECTOR,value='#root > div > div.header__conts > div.header__contInners > div > ul > li.sc-cZMNgc.dCkKyZ > span.sc-jQrDum.gMuQGX')





