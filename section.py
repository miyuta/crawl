import requests
from lxml.html import fromstring

session = requests.Session()

res = session.get('https://store.steampowered.com/search/?specials=1')

urls = fromstring(res.content)


for a in urls.xpath('//*[@id="search_resultsRows"]/a'):
    link = a.get('href')

for b in urls.cssselect('div#search_resultsRows a'):
    link2 = b.get('href')

    print(link2)