from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd



#convert url to html
# url = 'https://lots.impark.com/imp/en?latlng=49.895136,-97.138374&q=Winnipeg%20undefined%20undefined'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
driver = webdriver.Chrome(executable_path= './drivers/chromedriver')
driver.get('https://lots.impark.com/imp/en?latlng=49.895136,-97.138374&q=Winnipeg%20undefined%20undefined')

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
    address.append(a.text)

for p in prices:
    price_per_hour.append(p.text)
    
print(len(names))
print(len(address))
print(len(price_per_hour))
df = pd.DataFrame({'Lot Name': names, 'Address': address, 'Price': price_per_hour})
df.to_csv('winnipegparking.csv', index=False, encoding='utf-8')

# names.append(lot_names.text)
# address.append(addresses.text)
# price_per_hour.append(prices.text)


