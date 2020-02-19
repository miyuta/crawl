import requests
import lxml.html
from bs4 import BeautifulSoup as bs

# Session 設定
session = requests.Session()

# URL　設定
html = session.get('https://store.steampowered.com/search/?specials=1')

# Stringから　HTMLに　変換
lxml_parse = lxml.html.fromstring(html.content)

# CSSSelectでHTML要素を取得
for cssselect in lxml_parse.cssselect('div#search_resultsRows a'):
    urls = cssselect.get('href')
    print('Steam URL : {}'.format(urls))

print()
print()
print('Header Info : {}'.format(html.headers))