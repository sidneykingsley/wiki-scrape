from logging import log
import pandas as pd
from bs4 import NavigableString, Tag, Comment, BeautifulSoup 
from selenium import webdriver
import requests
# driver = webdriver.Chrome(executable_path='bin/chromedriver')
# driver.get('https://en.wikipedia.org/wiki/Thomas_H%C3%B6rster')
# html = driver.page_source
url = 'https://en.wikipedia.org/wiki/Thomas_H%C3%B6rster'
result = requests.get(url)
c = result.content
h_counter = 0
soup = BeautifulSoup(c, "html.parser")

for header in soup.find("div", {"class":"mw-parser-output"}).findAll('h2'):
    nextNode = header
    h_result = []
    h_result.append(nextNode.get_text(strip=True).strip())
    str_header_init = ''.join(str(e) for e in h_result)
    str_header = str_header_init.replace("[edit]","")
    print_results = []
    while True:
        nextNode = nextNode.nextSibling
        if nextNode is None:
            break
        if nextNode is Comment:
            break
        if isinstance(nextNode, Tag):
            print('--------checking--------')
            results = []
            if nextNode.name == "h2":
                break
            if nextNode.name == "p":
                article = []
                app_results = []
                results.append(nextNode.get_text)
                for x in results:
                    app_results.append(x.__self__)
                str_results = ''.join(str(e) for e in app_results)
                soup_results = BeautifulSoup(str_results, "html.parser")
                article = soup_results.findAll('p')
                print_results = []
                for x in article:
                    print_results.append(x.text)
                    print(x.text)
                
    df = pd.DataFrame({str_header: print_results})
    df.to_csv('gf_{0}.csv'.format(str_header), index=False, encoding='utf-8')
    h_counter += 1
    print('<<<<<<<<< one run >>>>>>>>>')