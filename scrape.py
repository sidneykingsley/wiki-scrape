import pandas as pd
from bs4 import BeautifulSoup 
from selenium import webdriver
import requests
driver = webdriver.Chrome(executable_path='bin/chromedriver')
driver.get('https://en.wikipedia.org/wiki/Ed_Sheeran')
html = driver.page_source
results = []
soup = BeautifulSoup(html, "html.parser")
article = soup.find("div", {"class":"mw-parser-output"}).findAll('p')
for newp in article:
    results.append(newp.text)
df = pd.DataFrame({'Body Text': results})
df.to_csv('sheeran.csv', index=False, encoding='utf-8')