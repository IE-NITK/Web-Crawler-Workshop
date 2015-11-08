__author__ = 'vidit'

from bs4 import BeautifulSoup
import urllib.request
import math

# The website is structured such a way that all gems are arranged alphabetically with each alphabet having multiple pages with 30 gems listed on each page
# On the header of each page it shows how many gems are there totally for each letter

list_of_gems = {}
for alphabet in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    page = urllib.request.urlopen("https://rubygems.org/gems?letter=" + alphabet).read()
    soup1 = BeautifulSoup(page, 'html.parser')
    total = soup1.find("p")
    total = total.contents[3]
    total = total.get_text()
    total = int(total)
    pages = math.ceil(total/30) + 1
    for i in range(1,pages):
        page_let = urllib.request.urlopen("https://rubygems.org/gems?letter=" + alphabet + "&page=" + str(i)).read()
        soup2 = BeautifulSoup(page_let, 'html.parser')
        name = soup2.findAll('a', {"class": "gems__gem"})
        for a in name:
            key = str(a.find('p', {"class": "gems__gem__downloads__count"}).contents[0])
            key = key.strip(" ")
            key = key.strip("\n")
            key = key.strip(" ")
            comma = key.find(",")
            while comma>=0:
                key = key[0:comma]+key[comma+1:]
                comma = key.find(",")
            key = int(key)
            value = str(a.div.h2.contents[0])
            value = value.strip(" ")
            value = value.strip("\n")
            value = value.strip(" ")
            list_of_gems.update({key:value})

for j in sorted(list_of_gems):
    print(list_of_gems[j] + " was downloaded " + str(j))






