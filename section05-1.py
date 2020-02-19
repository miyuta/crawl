# section05-1
# BeautifulSoup4

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

# Ex1(BeautifulSoup Basic)
# html = request.get('http://......')
soup = bs(html, 'html.parser')

# type
print('soup', type(soup))
# print('prettify', soup.prettify())

# h1 Tag
h1 = soup.html.body.h1
print('h1 : ', h1)

# p Tag
# Onliy first one
p1 = soup.html.body.p
print('p1 : ', p1)

# next p Tag
# first p = </br>
# third p = </br>
p2 = p1.next_sibling.next_sibling
print('p2 : ', p2)

# Text
print('h1 >>', h1.string)

# Text2
print('p1 >>', p1.string)

# module
# print(dir(p2))

# next Element
# print(p2.next_element)

for v in p2.next_element:
    pass
    # print(v)

# Ex2(find, find_all)

soup2 = bs(html, 'html.parser')

# a All Tag
# link1 = soup2.find_all('a', limit=2)
# link1 = soup2.find_all('a')

# type
# print(type(link1))

# list
# print('link : ', link1)

link2 = soup2.find_all('a', class_='sister') # id="link2", string="title", string=["Elsie"]
# link3 = soup2.find_all('a', string=["Elsie"])
# print(link3)

# for t in link2:
    # print(t)


link3 = soup2.find('a')

# print()
# print(link3)
# print(link3.string)
# print(link3.text)



# multiful
link4 = soup2.find("a", {"class":"sister", "data-io": "link3"})
print()
print(link4)
# print(link4.text)
print(link4.string)

# CSS selector : select, select_one
# Tag : find, find_all
# Ex3 select, select_one

link5 = soup.select_one('p.title > b')

print()
print(link5)
# print(link5.text)
print(link5.string)

link6 = soup.select_one("a#link1")

print()
print(link6)

link7 = soup.select_one('a[data-io="link3"]')

print()
print(link7) # .class #id  []

# All

link8 = soup.select('p.story > a')  # type: list

print()
print(link8)

for v in link8:
    print(v)


link9 = soup.select('p.story > a:nth-of-type(2)')

print()
print(link9)

link10 = soup.select('p.story')

print()
print(link10)
print()
print()

for t in soup.select('p.story'):
    temp = t.find_all('a')
    # print(temp)
    if temp:
        for v in temp:
            print(v)
    else:
        print(t)