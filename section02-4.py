# section02-4
# use lxml
# session - keep connection
# use xpath

# pip instal lxml, requests, cssselect 

import requests
from lxml.html import fromstring, tostring

def main():
    """
    main news scrapping
    """
    # use session
    session = requests.Session()

    # scrapping url
    response = session.get('https://www.naver.com') # GET, POST

    # link dictionary     scrape_news_list_page function call
    urls = scrape_news_list_page(response)

    # print dictionary
    # print(urls)

    # result
    for name, url in urls.items():
        # url
        print(name, url)

        # write

def scrape_news_list_page(response):
    #url dictionary
    urls = {}

    #tag string
    root = fromstring(response.content)
    
    for a in root.xpath('//ul[@class="api_list"]/li[@class="api_item"]/a[@class="api_link"]'):
        # a 구조확인
        # print(a)

        # a 문자열 출력
        # print(tostring(a, pretty_print=True))
        
        name, url = extract_contents(a)

        # 딕셔너리 삽입
        urls[name] = url

    return urls

def extract_contents(dom):
    # 링크 주소
    link = dom.get("href")

    # 신문사
    name = dom.xpath('./img')[0].get('alt') # xpath('./img)

    return name, link

# scrapping start
if __name__ == "__main__":
    main()