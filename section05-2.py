# section05-2
# beautifulSoup Scrapping - image Download

import os
import urllib.parse as par
import urllib.request as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs

# Header init
opener = req.build_opener()
# User-Agent
opener.addheaders = [('User-agent', UserAgent().chrome)]
# add Header
req.install_opener(opener)

# word for search
query = par.quote_plus('ライオンキング')

# image URL(chrome developer)
base = 'https://www.google.com/search?q=' + query +'&newwindow=1&rlz=1C1EXJR_koJP852JP852&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjfm-jzztjnAhVAx4sBHRIYDDwQ_AUoAXoECCAQAw&biw=1745&bih=881'

# URL
print('request URL: {}'.format(base))

res = req.urlopen(base)

# image save
savePath = 'f:/CrawlTest/imagedown/' # f:\\CrawlTest\\imagedown

# make folder + Exception
try:
    # folder check
    if not (os.path.isdir(savePath)):
        # make folder
        os.makedirs(os.path.join(savePath))
except OSError as e:
    # error
    print("folder creation failed.")
    print("folder name : {}".format(e.filename))

    # runtime error
    raise RuntimeError("system Exit!")
else:
    # make folder, exist folder
    print("folder is created.")


# bs4 init
soup = bs(res, 'html.parser')

# print(soup.prettify())

# select
# img_list = soup.select('div.isv-r.PNCib.MSM1fd.BUooTd > a.wXeWr.islib.nfEiy.mM5pbd > div.bRMDJf.islir')
img_list = soup.select('a.wXeWr > div.bRMDJf.islir > img')

# find_aa
img_list2 = soup.find_all('div', class_='bRMDJf islir')
for i ,v in enumerate(img_list2, 1):
    img_t = v.find('img')
    # print(img_t)
    # print(img_t.attrs['data-iurl'])
    fullFilename2 = os.path.join(savePath, savePath + str(2) +str(i) + '.png')
    req.urlretrieve(img_t.attrs['data-iurl'], fullFilename2)
# print(img_list)

# print(img_list)
# for i, img in enumerate(img_list, 1):
#     # Attribute
#     # print(img['data-iurl'], i)

#     # filename, path
#     fullFilename = os.path.join(savePath, savePath + str(i) + '.png')

#     # print(fullFilename)

#     # Download Request
#     req.urlretrieve(img['data-iurl'], fullFilename)

# print("download succeed.")