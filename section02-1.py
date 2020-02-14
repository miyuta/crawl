# section02-1
# use urllib

# google image Download
# google HTML Download
# header check
# download&save file

import urllib.request as req

#File url
img_url = 'https://t1.daumcdn.net/liveboard/thisisgame/f89efeb15ebf47c0aa1d97df2229d45b.JPG'
html_url = 'http://google.com'

#Download path
save_path1 = 'f:/test1.jpg'
save_path2 = 'f:/index.html'

#Exception
try:    # urlretrieve는 파라메터를 2개 받는다 1. 대상, 2. 경로
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print('Download Failed')
    print(e)
else:
    # Print Header
    print(header1)
    print(header2)

    #다운로드 파일 정보
    print('Filename {}'.format(file1))
    print('Filename {}'.format(file2))
    print()

    #success
    print('Download Secceed')

# content-type image/jpeg
# content type : text/html
# connection : close -> HTTP는 한번 연결되면 연결이 끊긴다.