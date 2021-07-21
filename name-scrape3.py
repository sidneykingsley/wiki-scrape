from logging import log
from bs4 import Tag, Comment, BeautifulSoup 
import requests
import os
import re
folder_name = 'names'
file_name = 'olympics.txt'
for x in range(7):
    i = x+1
    print(i)
    j = str(i)
    url = 'https://www.behindthename.com/namesakes/browse.php?type_list=1&operator_list=is&value_list[]=olympics&type_birthdate=1&operator_birthdate=more&value_birthdate[]=1980&sort=alpha&page='+j
    result = requests.get(url)
    c = result.content
    name = ''
    soup = BeautifulSoup(c, "html.parser")
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    main_file = open(folder_name+'/'+file_name, 'a')
    for header in soup.find("table", {"class":"r0r1"}).findAll('td'):
        htmlStr = str(header.text)
        name = re.sub("(?=\().*", "", htmlStr)
        name = re.findall("([A-Z].*)", name)
        if (name):
            main_file.write(name[0]+'\n')
            main_file = open(folder_name+'/'+file_name, 'a')
    