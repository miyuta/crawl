# section04-1
# requests scrapping - Session

import requests

# Activate Session
s = requests.session()

r = s.get('https://www.google.com')

# response data
print(r.text)

# Status 200,201,404.......
print('Status Code : {}'.format(r.status_code))

# check True, False
print('OK? : {}'.format(r.ok))

s = requests.session()

# cookie Return

r1 = s.get("https://httpbin.org/cookies", cookies={'name' : 'seo1'})
print(r1.text)

# cookie Set
r2 = s.get("https://httpbin.org/cookies/set", cookies={'name' : 'seo2'})
print(r2.text)


# User-agent
url = "https://httpbin.org"
headers = {'user-agent' : 'niceman_1.0.0_win10_ram16_home_chrome'}

# header request
r3 = s.get(url, headers=headers, cookies={'name' : 'seo1'})
# print(r3.text)

# Deactivate Session
s.close()

# with -> File, DB, HTTP
with requests.session() as s:
    r = s.get('https://www.google.com')
    # print(r.text)
    print(r.ok)



