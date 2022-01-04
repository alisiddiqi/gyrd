from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv


driver = webdriver.Chrome(executable_path= './drivers/chromedriver')
driver.get('https://en.parkopedia.ca/parking/locations/ottawa_ontario_canada_04f7f244mssjmfdcj0/?arriving=202201041600&leaving=202201041800')


list_of_addresses = []
price = []
duration = []

total_parking_spots = driver.find_elements(By.CLASS_NAME, 'LocationListItem__containerLink')

for parking_spot in total_parking_spots:
    try:
        line_name = parking_spot.find_element(By.CLASS_NAME, 'LocationListItem__title')
        line_duration = parking_spot.find_element(By.CLASS_NAME,'LocationDetailsSearchDetails__detail__label')
        line_price = parking_spot.find_element(By.CLASS_NAME, 'LocationDetailsSearchDetails__detail__value')
    except:
        line_price = None
        line_duration = None
    list_of_addresses.append(line_name.text + " Ottawa, ON")
    if not line_duration == None:
        duration.append(line_duration.text)
    else:
        duration.append("None")
    if not line_price == None:
        price.append(line_price.text)
    else:
        price.append("N/A")



df = pd.DataFrame({'Lot Name': list_of_addresses, 'Price': price, 'Duration': duration})
df.to_csv('OttawaParkopedia.csv', index=False, encoding='utf-8')
driver.quit()

# #hello

