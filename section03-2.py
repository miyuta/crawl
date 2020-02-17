# section03-1
# GET - RSS

import urllib.request
import urllib.parse

# https://library.maastrichtuniversity.nl/librarywall/collections/?_page=4
# 행정 안전부 https://www.mois.go.kr/

API = 'https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp'

params = []
for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))

# 중간 확인
# print(params)

# 연속 요청
for c in params:
    # 파라메터 출력
    # print(c)
    param = urllib.parse.urlencode(c)
    # print(param)
    # url 완성
    url = API + '?' + param
    # print("url :", url)

    # 요청
    res_data = urllib.request.urlopen(url).read()
    # print(res_data)

    # 수신 후 디코딩
    contents = res_data.decode("UTF-8")

    # 출력
    print(contents)