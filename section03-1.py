# section03-1
# GET - ipify

import urllib.request
from urllib.parse import urlparse

#request-1
url = "https://www.amazon.co.jp/"

# urlopen -> save
mem = urllib.request.urlopen(url)


# type : <class 'http.client.HTTPResponse'> 
print('type : {}'.format(type(mem)))

# geturl : https://www.amazon.co.jp/ url
print('geturl : {}'.format(mem.geturl()))

# status : 200
print('status : {}'.format(mem.status))

# headers : [('Date', 'Fri, 14 Feb 2020 15:02:33 GMT'), ('Set-Cookie', 'WMONID=5KjLc3zoslc; Expires=Sun, 14-Feb-2021 24:2:33 GMT; Path=/'), 
# ('Content-Type', 'text/html; charset=EUC-KR'), ('Connection', 'close'), ('Content-Language', 'ko-KR'), 
# ('Set-Cookie', 'JSESSIONID=1Q1aaml10vSnlZzmBpoWVBqKjbeED11pPUnr59Ej0CxkLmC04FrkSeSKgqqlHkMn.encarwas2_servlet_engine2;Path=/'), 
# ('P3P', "CP='CAO PSA CONi OTR OUR DEM ONL'"), ('X-UA-Compatible', 'IE=Edge'), ('Transfer-Encoding', 'chunked')]
print('headers : {}'.format(mem.getheaders()))

# getcode : 200
print('getcode : {}'.format(mem.getcode()))

# read : <!doctype html><html lang="ja-jp" class="a-no-js" data-19ax5a9jf="dingo"><!-- sp:feature:head-start
print('read : {}'.format(mem.read(100).decode('UTF-8')))

# parse : ParseResult(scheme='https', netloc='www.amazon.co.jp', path='', params='', query='test=test', fragment='')
print('parse : {}'.format(urlparse('https://www.amazon.co.jp?test=test')))

# parse : test=test
print('parse : {}'.format(urlparse('https://www.amazon.co.jp?test=test').query))

#request-2 ipify Request -> Response
API = "https://api.ipify.org"

# GET method parameter
values = {
    'format' : 'json'
}

print('before param : {}'.format(values))
param = urllib.parse.urlencode(values)
print('before param : {}'.format(param))

url = API + '?' + param

print('request url = {}'.format(url))

# response read
data = urllib.request.urlopen(url).read()

# response decode
text = data.decode('UTf-8')
print('response : {}'.format(text))