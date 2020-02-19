from bs4 import BeautifulSoup as bs

html = """
<html>
    <head>
    <title>The Dormouse's Story</title>
    </head>
    <body>
        <h1>This is h1 area</h1>
        <h2>This is h2 area</h2>
        <p class="title"><b>The Dormouse's Story</b></p>
        <p class="story">Once upon a time there were three little sisters.
            <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            <a data-io="link3" href="http://example.com/little" class="sister" id="link3">Title</a>
        </p>
        <p class="story">
            story.....
        </p>
    </body
</html>
"""
soup = bs(html, 'html.parser')

# 選択した全ての要素取得
Ex1 = soup.find_all('a', class_ ='sister')
print(Ex1)

# 選択した要素の中で最初に見つけた1番目の要素取得
Ex2 = soup.find("a", {"class":"sister"})
print()
print(Ex2)

# 選択した要素の中で最初に見つけた1番目の要素取得
Ex3 = soup.select_one('p.title > b')
print()
print(Ex3)

# 選択した全ての要素取得
Ex4 = soup.select('p.story > a')
print()
print(Ex4)