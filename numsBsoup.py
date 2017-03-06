import urllib.request
import bs4 as bs
import re
url = 'http://python-data.dr-chuck.net/comments_338096.html'

sauce = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(sauce, 'html.parser')

numList = list()

tags = soup('span')

for tag in tags:
    y = str(tag)
    x = re.findall('[0-9]+',y)
    for i in x:
        i = int(i)
        numList.append(i)


print ( 'There are ' + str(len(numList)) + ' numbers in this list and their total sum is ' + str(sum(numList)))


# print(numList)
