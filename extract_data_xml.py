from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

URL = input('Enter URL: ')

xml = urlopen(URL, context = ctx).read()

tree = ET.fromstring(xml)

counts = tree.findall('.//count')

total = 0

for count in counts:
    num = int(count.text)
    total = total + num

print ('Retrieved', len(xml), 'characters')
print ('Count is :', len(counts))
print ('Sum is :', total)
