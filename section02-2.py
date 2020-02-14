#section02-2
# urlopen

import urllib.request as req
from urllib.error import URLError, HTTPError

# Download path, filename

path_list = ['f:/test2.jpg', 'f:/index1.html']

# Download resources url
target_url = ['https://t1.daumcdn.net/thumb/R1000x0/?fname=https://i.imgur.com/VA9n37G.jpg', 'http://gpogle.com']

for i, url in enumerate(target_url):
    #exception
    try:
        # url read
        response = req.urlopen(url)
        content = response.read()

        print('----------------------------------------------------------------')

        #State
        print('header Info-{} : {}'.format(i, response.info()))
        print('HTTP Status Code : {}'.format(response.getcode()))
        print()
        print('----------------------------------------------------------------')

        # Download Save   wb = write byte
        with open(path_list[i], 'wb') as c:
            c.write(content)
        
    except HTTPError as e:
        print('Download failed.')
        print('HTTPError code : ', e.code)
    except URLError as e:
        print('download failed.')
        print('URL Error reason : ', e.reason)
    #Success
    else:
        print()
        print("Download Succeed.")
