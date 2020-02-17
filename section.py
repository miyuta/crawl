import requests
import lxml.html


def main():

    session = requests.Session()

    response = session.get('https://store.steampowered.com/search/?specials=1')

    urls_xpath = scrapig_steam_xpath(response)
    urls_cssselect = scraping_steam_cssselect(response)

    for url_xpath in urls_xpath:
        print(url_xpath)

    print('----------------------------------------------------------------------------------------------------')
    print('----------------------------------------------------------------------------------------------------')

    for url_cssselect in urls_cssselect:
        print(url_cssselect)


def scrapig_steam_xpath(response):
    urls = []

    root = lxml.html.fromstring(response.content)

    for a in root.xpath('//*[@id="search_resultsRows"]/a'):
        link = a.get('href')
        urls.append(link)
        # print(link)
    return urls


def scraping_steam_cssselect(response):
    urls = []

    root = lxml.html.fromstring(response.content)

    for b in root.cssselect('div#search_resultsRows a'):
        link2 = b.get('href')
        urls.append(link2)
        print(link2)
    return urls

if __name__ == '__main__':
    main()