import urllib.request as req
import requests

# URL　設定
img_url = 'https://img.sbs.co.kr/newimg/news/20181123/201253168_1280.jpg'

# ダウンロードPATH　設定
save_path1 = 'f:/test1.jpg'

# ダウンロード開始
file1, header1 = req.urlretrieve(img_url, save_path1)

# Header　確認
print(header1)