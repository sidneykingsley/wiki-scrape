from logging import log
from bs4 import Tag, Comment, BeautifulSoup 
import requests
import os
import re
folder_name = 'names'
file_name = 'athletes.txt'
url = 'https://bleacherreport.com/articles/741676-the-100-most-beloved-athletes-in-sports-history'
result = requests.get(url)
c = result.content
h_counter = 0
name = ''
soup = BeautifulSoup(c, "html.parser")
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
main_file = open(folder_name+'/'+file_name, 'a')
for header in soup.find("div", {"id":"page-content"}).findAll('h1'):
    htmlStr = str(header)
    name = re.sub("\<h1\>([^\s]+)", "", htmlStr)
    name = re.sub("\<\/h1\>", "", name)
    main_file.write(name+'\n')
    main_file = open(folder_name+'/'+file_name, 'a')
    