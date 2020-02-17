# section03-3
# fake-useragent
# Stock data

import json
import urllib.request as req
from fake_useragent import UserAgent
import csv

# Fake Header정보(가상 user-agent)
ua = UserAgent()

print(ua.ie)
print(ua.msie)
print(ua.chrome)
print(ua.safari)
print(ua.random)

# User-agent header
headers = {
    'User-agent': ua.ie,
    'referer': 'http://finance.daum.net/'
}

# request URL

url = 'http://finance.daum.net/api/search/ranks?limit=10'

# request
res = req.urlopen(req.Request(url, headers=headers)).read().decode('UTF-8')

# 응답 데이터 확인(Json Data)
# print('res', res)

# 응답 데이터 String -> json 변환 및 data 값 출력
rank_json = json.loads(res)['data']
print(rank_json)

# 중간 확인
# print(rank_json, '\n')

path = 'f:/CrawlTest/test.txt'
path_csv = 'f:/CrawlTest/test.csv'
txt_rank = ""
list_rank = []
for elm in rank_json:
    # print(type(elm))
    # Save TXT File
    txt_rank += ('순위 : {}, 금액 : {}, 회사명 : {}\n'.format(elm['rank'], elm.get('tradePrice'), elm['name']))

    with open(path, mode='wt', encoding='UTF-8') as c:
        c.write(txt_rank)

    # Save CSV File
    wordSplte = ('순위,{},금액,{},회사명,{}'.format(elm['rank'], elm.get('tradePrice'), elm['name'])).split(',')
    list_rank.append(wordSplte)

# print(list_rank)
with open(path_csv, mode='w', encoding='EUC-KR', newline='') as c:
    mkCsv = csv.writer(c)

    for stock in list_rank:
        print(stock)
        mkCsv.writerow(stock)