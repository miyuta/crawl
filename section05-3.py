# section05-3
# Beautifulsoup scrapping - login

import requests as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs

login_info = {
    'redirectUrl': 'http://www.danawa.com/',
    'loginMemberType': 'general',
    'id': 'miyuta@hanmail.net',
    'password': '1377kulu@'
}

# Headers
headers = {
    "User-Agent" : UserAgent().chrome,
    "Referer": 'https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2F'
}

with req.session() as s:
    # request(login)
    res = s.post('https://auth.danawa.com/login', login_info, headers=headers)

    # login fail Exception
    if res.status_code != 200:
        raise Exception("login failed")

    # Request Data
    # print(res.content.decode('UTF-8'))
    
    # move with session(headers)
    res = s.get('https://buyer.danawa.com/order/Order/orderList', headers=headers)
    
    # EUC-KR
    # res.encodung = 'EUC-KR'

    # request Data
    # print(res.text)

    # bs4 init
    soup = bs(res.text, 'html.parser')

    # login ckeck
    check_name = soup.find('p', class_= 'user')
    # print(check_name)

    if check_name is None:
        raise Exception('login failed. Wrong Password.')

    # select
    info_list = soup.select('div.my_info > div.sub_info > ul.info_list > li')
    print(info_list)

    # re-request, Download, save file, DB.....
    print()
    print("***** My Info *****")

    for v in info_list:
        # attrs
        # print(dir(v))

        # Text
        proc, val = v.find('span').string.strip(), v.find('strong').string.strip()
        print('{} : {}'.format(proc, val))