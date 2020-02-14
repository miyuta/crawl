# section02-4
# use lxml
# session - keep connection

#pip instal lxml, requests, cssselect 

import requests
from lxml.html import fromstring, tostring

def main():
    """
    main news scrapping
    """
    # use session
    session = requests.Session()

    # scrapping url
    res = session.get('https://www.naver.com') # GET, POST

    # link list     scrape_news_list_page function call
    urls = scrape_news_list_page(res)

    # result
    for url in urls:
        # url
        print(url)

        # write

def scrape_news_list_page(response):
    #url list
    urls = []

    #tag string
    root = fromstring(response.content)

    for a in root.cssselect('.api_list .api_item a.api_link'):
        #link
        url = a.get('href')
        # for문 돌면서 하나씩 urls 리스트에 담긴다.
        urls.append(url)
    return urls

# scrapping start
if __name__ == "__main