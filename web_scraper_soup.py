from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urlopen('http://py4e-data.dr-chuck.net/comments_42.html').read()

soup = BeautifulSoup(html, "html.parser")

tags = soup('span')

total = 0

for tag in tags:
    num = tag.contents[0]
    total = total + int(num)

print(total)
