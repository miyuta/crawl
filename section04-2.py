# section04-2
# requests scrapping2 - JSON
# https://httpbin.org

import json
import requests

s = requests.session()

# 100개 요청
# 텍스트 형태 데이터 가져올때 stream
r = s.get('https://httpbin.org/stream/1', stream=True)

# 수신 확인
print(r.text)

# encoding
print('Before Encoding : {}'.format(r.encoding))

if r.encoding is None:
    r.encoding = 'UTF-8'

print('After Encoding : {}'.format(r.encoding))


for line in r.iter_lines(decode_unicode=True):
    # 라인 출력 후 타입 확인
    # print(line)
    # print(type(line))

    #JSON(dict) 변환 후 확인
    b = json.loads(line) # String -> dictionary
    print(b)
    # print(type(b))

    for k, v in b.items():
        print('key : {}, value : {}'.format(k, v))
        if k == 'headers':
            for k2, v2 in v.items():
                print('key2 :{}, value2 : {}'.format(k2, v2))
            continue        
    print()
    print()
    print()

s.close()

r = s.get("https://jsonplaceholder.typicode.com/todos/1")

# Header 정보
print(r.headers)

# 본문 정보
print(r.text)

# JSON 변환
print(r.json())

# 키
print(r.json().keys())

# 값
print(r.json().values())

# 인코딩
print(r.encoding)

# 바이너리
print(r.content)

s.close()