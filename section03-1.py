# section03-1
# GET

import urllib.request
from urllib.parse import urlparse

# #request-1
# url = "http://www.encar.com"

# # urlopen 수신된 정보 저장
# mem = urllib.request.urlopen(url)

# # 여러 정보

# # type : <class 'http.client.HTTPResponse'> 종류
# print('type : {}'.format(type(mem)))

# # geturl : http://www.encar.com/index.do url
# print('geturl : {}'.format(mem.geturl()))

# # status : 200
# print('status : {}'.format(mem.status))

# # headers : [('Date', 'Fri, 14 Feb 2020 15:02:33 GMT'), ('Set-Cookie', 'WMONID=5KjLc3zoslc; Expires=Sun, 14-Feb-2021 24:2:33 GMT; Path=/'), 
# # ('Content-Type', 'text/html; charset=EUC-KR'), ('Connection', 'close'), ('Content-Language', 'ko-KR'), 
# # ('Set-Cookie', 'JSESSIONID=1Q1aaml10vSnlZzmBpoWVBqKjbeED11pPUnr59Ej0CxkLmC04FrkSeSKgqqlHkMn.encarwas2_servlet_engine2;Path=/'), 
# # ('P3P', "CP='CAO PSA CONi OTR OUR DEM ONL'"), ('X-UA-Compatible', 'IE=Edge'), ('Transfer-Encoding', 'chunked')]
# print('headers : {}'.format(mem.getheaders()))

# # getcode : 200
# print('getcode : {}'.format(mem.getcode()))

# print('read : {}'.format(mem.read(100).decode('UTF-8')))

# # parse : ParseResult(scheme='http', netloc='www.encar.co.kr', path='', params='', query='test=test', fragment='')
# print('parse : {}'.format(urlparse('http://www.encar.co.kr?test=test')))

# # parse : test=test
# print('parse : {}'.format(urlparse('http://www.encar.co.kr?test=test').query))

#request-2 ipify 요청하면 리턴해줌
API = "https://api.ipify.org"

# GET 방식 파라메터
values = {
    'format' : 'json'
}

print('before param : {}'.format(values))
param = urllib.parse.urlencode(values)
print('before param : {}'.format(param))

url = API + '?' + param

print('요청 url = {}'.format(url))

# 수신 데이터 읽기
data = urllib.request.urlopen(url).read()

# 수신 데이터 디코딩
text = data.decode('UTf-8')
print('response : {}'.format(text))