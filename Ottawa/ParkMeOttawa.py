from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import time

#retrieve website, based on selenium's driver
driver = webdriver.Chrome(executable_path= './drivers/chromedriver')
driver.get('https://www.parkme.com/ottawa-on-parking')
time.sleep(5)

#columns names for csv
lot_name = []
lot_address = []
price = []
duration = []

total_parking_spots = driver.find_elements(By.CLASS_NAME, 'featured_lot_container')
print(len(total_parking_spots))

for parking_spot in total_parking_spots:
        line_name = parking_spot.find_element(By.CLASS_NAME, 'fle_lot_name')
        try:
            line_address = parking_spot.find_element(By.CLASS_NAME, 'fle_lot_address')
        except:
            line_address = None
        try:
            line_price = parking_spot.find_element(By.CSS_SELECTOR, "a[class='left btn btn-primary btn-small fle_reserve compare-res-btn']")
        except:
            line_price = None
        lot_name.append(line_name.text)
        lot_address.append(line_address.text + ", Ottawa, ON")
        if not line_price == None:
            duration.append("1 hour")
            price.append(line_price.text)
        else:
            duration.append("None")
            price.append("N/A")

df = pd.DataFrame({'Lot Address': lot_address, 'Lot Name': lot_name, 'Price': price, 'Duration': duration})
df.to_csv('OttawaParkMe.csv', index=False, encoding='utf-8')


