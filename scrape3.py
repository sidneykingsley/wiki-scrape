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

for header in soup.find_all('h2'):
    nextNode = header
    while True:
        nextNode = nextNode.nextSibling
        if nextNode is None:
            break
        if nextNode is Comment:
            break
        if isinstance(nextNode, Tag):
            h_result = []
            results = []
            if nextNode.name == "h2":
                h_result.append(nextNode.get_text(strip=True).strip())
                print('___title___')
                for i in h_result:
                    print(i)
                break
            if nextNode.name == "p":
                article = []
                app_results = []
                results.append(nextNode.get_text)
                # str_results = ''.join(str(e) for e in results)
                for x in results:
                    # print(x.__self__)
                    app_results.append(x.__self__)
                # str1 = ''.join(results)
                # print(app_results)
                str_results = ''.join(str(e) for e in app_results)
                soup_results = BeautifulSoup(str_results, "html.parser")
                # print(soup_results)
                article = soup_results.findAll('p')
                print_results = []
                for x in article:
                    print_results.append(x.text)
                    print(x.text)
                df = pd.DataFrame({'Body Text': print_results})
                df.to_csv('gf{0}.csv'.format(h_counter), index=False, encoding='utf-8')
                h_counter += 1
            print('---------one instance--------')
            # str_results = ''.join(str(e) for e in results)
            # soup_results = BeautifulSoup(str_results, "html.parser")
            # article = soup_results.findAll('p')
            # print(article)
            # for x in article:
            #     print('HELLO?????')
                # presults.append(x.text)
            # print('presults')
            # print(presults)
            # for x in presults:
            #     print(presults)
            # for i in article:
            #     print(i)

            # for x in results:
            #     print(x)
            # df = pd.DataFrame({'Body Text': presults})
            # df.to_csv('newguy{0}.csv'.format(thisDude), index=False, encoding='utf-8')

# for x in article:
#     print(x.text)

                # presults.append(x.text)

            # presults = []
            # fres = ''.join(str(e) for e in results)
            # tres = BeautifulSoup(fres, "html.parser")
            # article = soup.find_all('p')
            # for i in article:
            #     print(i)
