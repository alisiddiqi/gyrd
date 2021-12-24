from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path= './drivers/chromedriver')
driver.get('https://spothero.com/search?kind=city&id=420&starts=2021-12-22T18%3A30&ends=2021-12-22T21%3A30')
time.sleep(1)
button = driver.find_element(By.XPATH, '//*[@id="pageScrollWrapper"]/div[3]/div/div[2]/div[2]/div/div/div/div/div/div/div[13]/div/div[2]/div/button[2]')
button.click()
button.click()
button.click()
button.click()
time.sleep(2)


names = []
price_per_hour = []

content = driver.page_source
soup = BeautifulSoup(content)
lot_names = soup.findAll('div', attrs={'class':'brand-button__text'})
prices = soup.findAll('span', attrs={'class':'text-small'})


for name in lot_names:
    if name not in names:
        names.append(name.text)


for p in prices:
    price_per_hour.append(p.text)
    
print(len(names))
print(len(price_per_hour))
df = pd.DataFrame({'Lot Name': names, 'Price': price_per_hour})
df.to_csv('EdmontonIndigo.csv', index=False, encoding='utf-8')

driver.quit()
#hello
