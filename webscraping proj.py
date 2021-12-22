from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


driver = webdriver.Chrome(executable_path= './drivers/chromedriver')
driver.get('https://lots.impark.com/imp/en?latlng=53.546125,-113.493823&q=Edmonton%20undefined%20undefined')

names = []
address = [] #address of parking spots
price_per_hour = []

content = driver.page_source
soup = BeautifulSoup(content)
lot_names = soup.findAll('div', attrs={'class':'lot-name'})
addresses = soup.findAll('span', attrs={'class':'address-text'})
prices = soup.findAll('div', attrs={'class':'lot-rate'})


for name in lot_names:
    names.append(name.text)

for a in addresses:
    address.append(a.text + "Edmonton, AB")

for p in prices:
    price_per_hour.append(p.text)
    
print(len(names))
print(len(address))
print(len(price_per_hour))
df = pd.DataFrame({'Lot Name': names, 'Address': address, 'Price': price_per_hour})
df.to_csv('EdmontonImPark.csv', index=False, encoding='utf-8')


#hello
