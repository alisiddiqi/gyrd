from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path= './drivers/chromedriver')
driver.get('https://en.parkopedia.ca/parking/locations/ottawa_ontario_canada_04f7f244mssjmfdcj0/?arriving=202201041600&leaving=202201041800')

list_of_addresses = []
price = []
duration = []

total_parking_spots = driver.find_elements(By.CLASS_NAME, 'LocationListItem__containerLink')

for parking_spot in total_parking_spots:
        line_name = parking_spot.find_element(By.CLASS_NAME, 'LocationListItem__title')
        try:
          line_duration = parking_spot.find_element(By.CLASS_NAME,'LocationDetailsSearchDetails__detail__label')
        except:
            line_duration = None
        try:
            line_price = parking_spot.find_element(By.CLASS_NAME, 'LocationDetailsSearchDetails__detail__value')
        except:
            line_price = None
        list_of_addresses.append(line_name.text + " Ottawa, ON")
        if not line_duration == None and not line_price == None:
            duration.append(line_duration.text)
            price.append(line_price.text)
        else:
            duration.append("None")
            price.append("N/A")



df = pd.DataFrame({'Lot Name': list_of_addresses, 'Price': price, 'Duration': duration})
df.to_csv('OttawaParkopedia.csv', index=False, encoding='utf-8')
driver.quit()

# #hello

