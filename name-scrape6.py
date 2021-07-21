from logging import log
from bs4 import Tag, Comment, NavigableString, BeautifulSoup 
import requests
import os
import re
folder_name = 'riasec-names'
file_name = 'c.txt'
url = 'https://www.behindthename.com/namesakes/list/evildoers/alpha'
result = requests.get(url)
c = result.content
name = ''
soup = BeautifulSoup(c, "html.parser")
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
main_file = open(folder_name+'/'+file_name, 'a')
for header in soup.find("table", {"class":"r0r1"}).findAll('tr'):
    tdCount = 0
    for td in header:
        if (tdCount == 0):
            main_file.write(td.text+'\n')
            main_file = open(folder_name+'/'+file_name, 'a')
        tdCount += 1
    