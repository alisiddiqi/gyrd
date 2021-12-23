from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path= './drivers/chromedriver')
driver.get('https://lots.impark.com/imp/en?latlng=53.540518,-113.499025&q=Edmonton%20AB%20Canada')
time.sleep(1)
button = driver.find_element(By.XPATH, '//*[@id="mapCanvas"]/div/div/div[13]/div/div[2]/div/button[2]')
button.click()
button.click()
# button.click()
# print(button)
time.sleep(2)


names = []
address = [] #address of parking spots
price_per_hour = []

content = driver.page_source
soup = BeautifulSoup(content)
lot_names = soup.findAll('div', attrs={'class':'lot-name'})
addresses = soup.findAll('span', attrs={'class':'address-text'})
prices = soup.findAll('div', attrs={'class':'lot-rate'})


for name in lot_names:
    if name not in names:
        names.append(name.text)

for a in addresses:
    address.append(a.text + "Edmonton, AB")

for p in prices:
    price_per_hour.append(p.text)
    
print(len(names))
print(len(address))
print(len(price_per_hour))
df = pd.DataFrame({'Lot Name': names, 'Address': address, 'Price': price_per_hour})
df.to_csv('EdmontonImPark3.csv', index=False, encoding='utf-8')


#hello
