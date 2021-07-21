import pandas as pd
from bs4 import BeautifulSoup 
from selenium import webdriver
import requests
driver = webdriver.Chrome(executable_path='bin/chromedriver')
driver.get('https://en.wikipedia.org/wiki/Thomas_H%C3%B6rster')
html = driver.page_source
tresults = []
soup = BeautifulSoup(html, "html.parser")
title = soup.find("div", {"class":"mw-parser-output"}).findAll('h2')
for newt in title:
    article = soup.find("div", {"class":"mw-parser-output"}).findAll('p')
    presults = []
    for newp in article:
        presults.append(newp.text)
    df = pd.DataFrame({'Body Text': presults})
    df.to_csv('TH-{0}.csv'.format(newt.text), index=False, encoding='utf-8')
