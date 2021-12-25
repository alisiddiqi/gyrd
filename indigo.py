from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



driver = webdriver.Chrome(executable_path= './drivers/chromedriver')
driver.get('https://ca.parkindigo.com/en/')
driver.implicitly_wait(5)
typing = driver.find_element_by_xpath('//*[@id="react-select-2-input"]')
typing.send_keys('Edmonton AB')
time.sleep(2)
typing.send_keys(Keys.ENTER)
time.sleep(2)
button = driver.find_element(By.XPATH, '//*[@id="pageScrollWrapper"]/div[3]/div/div[2]/div[2]/div/div/div/div/div/div/div[13]/div/div[2]/div/button[2]')
button.click()
button.click()
button.click()
time.sleep(15)


list_of_addresses = []
price_per_hour = []

lot_names = driver.find_elements_by_xpath('//*[@id="pageScrollWrapper"]/div[3]/div/div[2]/div[1]/div/div[2]/div[2]/div/a/div[1]')
prices = driver.find_elements_by_xpath('//*[@id="pageScrollWrapper"]/div[3]/div/div[2]/div[1]/div/div[2]/div[2]/div/div/a/div/span[2]')
for name in lot_names:
        list_of_addresses.append(name.text)


for p in prices:
    price_per_hour.append(p.text)
    
print(len(list_of_addresses))
print(len(price_per_hour))
print(list_of_addresses)
print(price_per_hour)
# df = pd.DataFrame({'Lot Name': names, 'Price': price_per_hour})
# df.to_csv('EdmontonIndigo.csv', index=False, encoding='utf-8')
#driver.quit()

# #hello

