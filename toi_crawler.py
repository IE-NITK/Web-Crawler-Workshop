from datetime import datetime
from threading import Timer
from bs4 import BeautifulSoup
import urllib.request


def retrieve():
    page = urllib.request.urlopen("http://timesofindia.indiatimes.com").read()
    soup = BeautifulSoup(page, 'html.parser')
    curr = datetime.today()
    print(curr)
    # name = soup.findAll('div', {"class": "top-story"})
    for i in range(2, 9):
        pg = "new_tops#" + str(i)
        name = soup.find('a', {"pg": pg}).contents[0]
        # name = name.contents
        print(name)
    # curr = datetime.today()
    nextday = curr.replace(day=curr.day + 1, hour=10, minute=0, second=0, microsecond=0)
    delta = nextday - curr
    sec = delta.seconds + 1
    t = Timer(sec, retrieve)
    t.start()


retrieve()
