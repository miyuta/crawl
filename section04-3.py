# section04-3
# request - REST API

# REST API : GET, POST, DELETE, PUT: UPDATE, REPLACE(FETCH : UPDATE, MODIFY)
# URL을 활용해서 자원의 상태 정보를 주고 받는 모든 것을 의미
# Requests Method 간단히 사용가능
import requests

# Session
s = requests.Session()

# Ex1
r = s.get('Https://api.github.com/events')

# Status check
r.raise_for_status()

# print(r.text)

# Ex2
jar = requests.cookies.RequestsCookieJar()

# cookie
jar.set('name', 'niecman', domain='httpbin.org', path='/cookies')

r = s.get('http://httpbin.org/cookies', cookies=jar)

# print(r.text)

# Ex3
r = s.get('https://github.com', timeout=5)

# print(r.text)

# Ex4
r = s.post('http://httpbin.org/post', data={'id':'test123', 'pw': '111'}, cookies=jar)

# print(r.text)
print(r.headers)

# Ex5
# POST
payload1 = {'id':'test123', 'pw':'111'}
payload2 = (('id','test123'), ('pw','222'))

r = s.post('http://httpbin.org/post', data=payload2)

print(r.text)

# Ex6
# PUT
r = s.put('http://httpbin.org/put', data=payload1)

print(r.text)

# Ex7
# DELETE
r = s.delete('http://httpbin.org/delete', data={'id': 1})

print(r.text)

r = s.delete('https://jsonplaceholder.typicode.com/posts/1')
print(r.text)
print(r.ok)
print(r.headers)
s.close()
