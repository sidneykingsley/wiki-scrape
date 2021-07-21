from logging import log
from bs4 import Tag, Comment, BeautifulSoup 
import requests
import os
import csv
folder_name = 'results'
file_name = 'wiki-m3.txt'
count = 1
with open('names/musicians.csv', newline='') as f:
    reader = csv.reader(f)
    names = list(reader)
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
main_file = open(folder_name+'/'+file_name, 'a')
for x in names:
    fname = x[0]
    sname = x[1]
    sname = sname.strip()
    name = fname+'_'+sname
    print('(',count, '/ 369 )')
    count += 1
    url = 'https://en.wikipedia.org/wiki/'+name
    try:
        result = requests.get(url)
        c = result.content
        h_counter = 0
        soup = BeautifulSoup(c, "html.parser")
        results = []
        app_results = []
        try:
            for main_cont in soup.find("div", {"class":"mw-parser-output"}).findAll('table', {"class":"vcard"}):
                mc_node = main_cont
                while True:
                    mc_node = mc_node.nextSibling
                    if mc_node is None:
                        break
                    if mc_node is Comment:
                        break
                    if isinstance(mc_node, Tag):
                        if mc_node.name == "div":
                            break
                        if mc_node.name == "p":
                            results.append(mc_node.get_text)
            for x in results:
                app_results.append(x.__self__)
            str_results = ''.join(str(e) for e in app_results)
            plhold_results = str_results.replace(fname, 'firstnameplaceholder')
            ammnded_results = plhold_results.replace(sname, 'secondnameplaceholder')
            soup_results = BeautifulSoup(ammnded_results, "html.parser")
            article = soup_results.findAll('p')
            print_results = []
            if article:
                main_file.write('\n(!!)Article(!/!)\n')
                main_file = open(folder_name+'/'+file_name, 'a')
            for x in article:
                i = x.text
                j = str(i)
                main_file.write(j.strip())
            for header in soup.find("div", {"class":"mw-parser-output"}).findAll('h2'):
                nextNode = header
                h_result = []
                h_result.append(nextNode.get_text(strip=True).strip())
                str_header_init = ''.join(str(e) for e in h_result)
                str_header = str_header_init.replace("[edit]","")
                print_results = []
                results = []
                article = []
                app_results = []
                while True:
                    nextNode = nextNode.nextSibling
                    if nextNode is None:
                        break
                    if nextNode is Comment:
                        break
                    if isinstance(nextNode, Tag):
                        if nextNode.name == "h2":
                            break
                        if nextNode.name == "p":
                            results.append(nextNode.get_text)
                for x in results:
                    app_results.append(x.__self__)
                str_results = ''.join(str(e) for e in app_results)
                plhold_results = str_results.replace(fname, 'firstnameplaceholder')
                ammnded_results = plhold_results.replace(sname, 'secondnameplaceholder')
                soup_results = BeautifulSoup(ammnded_results, "html.parser")
                article = soup_results.findAll('p')
                emptHeaders = ['External links', 'References', 'Bibliography']
                if article and str_header not in emptHeaders:
                    main_file.write('\n<h2>'+str_header+'</h2>\n')
                    main_file = open(folder_name+'/'+file_name, 'a')
                for x in article:
                    i = x.text
                    j = str(i)
                    main_file.write(j.strip())
                h_counter += 1
        except AttributeError:
            print("probs")
    except requests.ConnectionError as exception:
        print("URL does not exist on Internet")
