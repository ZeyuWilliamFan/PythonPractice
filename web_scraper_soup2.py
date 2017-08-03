from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

URL = input('Enter URL:')
count = int(input('Enter count:'))
position = int(input('Enter position:'))
final_name = None

for i in range(count):
    html = urlopen(URL, context = ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    tag = tags[position-1]

    if (i == count-1):
        final_name = tag.contents[0]

    URL = tag.get('href', None)

print (final_name)
