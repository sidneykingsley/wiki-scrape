from logging import log
import pandas as pd
from bs4 import NavigableString, Tag, Comment, BeautifulSoup 
import requests
import os
import numpy as np
import csv
with open('musician-names.csv', newline='') as f:
    reader = csv.reader(f)
    names = list(reader)
for x in names:
    fname = x[0]
    sname = x[1]
    sname = sname.strip()
    print(fname+' '+sname)
    name = fname+'_'+sname
    url = 'https://en.wikipedia.org/wiki/'+name
    result = requests.get(url)
    c = result.content
    h_counter = 0
    soup = BeautifulSoup(c, "html.parser")
    results = []
    app_results = []
    for main_cont in soup.find("div", {"class":"mw-parser-output"}).findAll('table'):
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
    for x in article:
        print_results.append(x.text)
    while print_results:
        df = pd.DataFrame({'Main': print_results})
        if not os.path.exists('musicians'):
            os.makedirs('musicians')
        with open('musicians'+'/Main.txt', 'a') as f:
            f.write(
                df.to_string(header = False, index = False)
            )
        break

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
        print_results = []
        for x in article:
            print_results.append(x.text)
        while print_results:
            df = pd.DataFrame({str_header: print_results})
            if not os.path.exists('musicians'):
                os.makedirs('musicians')
            with open('musicians'+'/'+str_header+'.txt', 'a') as f:
                f.write(
                    df.to_string(header = False, index = False)
                )
            break
        h_counter += 1

            
    
# table class="infobox biography vcard" to div class="toclimit-3"
