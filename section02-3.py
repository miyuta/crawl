# section02-3
# use lxml

#pip instal lxml, requests, cssselect 

import requests
import lxml.html

def main():
    """
    main news scrapping
    """

    #scrapping url
    response = requests.get('https://www.naver.com') # GET, POST

    #link list     scrape_news_list_page function call
    urls = scrape_news_list_page(response)

    # result
    for url in urls:
        # url
        print(url)

        # write

def scrape_news_list_page(response):
    # url list
    urls = []

    # tag string
    # <Element html at 0x183f955f728>
    root = lxml.html.fromstring(response.content)

    for a in root.cssselect('.api_list .api_item .api_link'):
        # link
        url = a.get('href')
        # print(url)
        # for문 돌면서 하나씩 urls 리스트에 담긴다.
        urls.append(url)
    return urls

# scrapping start
if __name__ == "__main__":
    main()