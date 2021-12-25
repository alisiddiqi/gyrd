from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv


driver = webdriver.Chrome(executable_path= './drivers/chromedriver')
driver.get('https://en.parkopedia.ca/parking/locations/edmonton_alberta_canada_7433c3x291cfrgz2j9/?country=ca&arriving=202112291300&leaving=202112291400')


list_of_addresses = []
price_per_hour = []

content = driver.page_source
soup = BeautifulSoup(content)

lines = driver.find_elements_by_class_name('LocationListItem__containerLink')

for line in lines:
    try:
        line_name = line.find_element_by_class_name('LocationListItem__title')
        line_price = line.find_element_by_class_name('LocationDetailsSearchDetails__detail__value')
    except:
        prices = ''
    list_of_addresses.append(line_name.text + " Edmonton, AB")
    price_per_hour.append(line_price.text)
  
print(len(list_of_addresses))
print(len(price_per_hour))

# lot_names = soup.findAll('h3', attrs={'class':'LocationListItem__title'})
# prices = soup.findAll('span', attrs={'class':'LocationDetailsSearchDetails__detail__value'})

# for name in lot_names:
#         list_of_addresses.append(name.text)

# for p in prices:
#     price_per_hour.append(p.text)



dictionary = dict(zip(list_of_addresses, price_per_hour))

# for key in dictionary:
#     if key in "ImPark":
#         del dictionary[key]



a_file = open("EdmontonParkopedia.csv", "w")

writer = csv.writer(a_file)
for key, value in dictionary.items():
    writer.writerow([key, value])

# df = pd.DataFrame({'Lot Name': names, 'Price': price_per_hour})
# df.to_csv('EdmontonIndigo.csv', index=False, encoding='utf-8')
driver.quit()

# #hello

