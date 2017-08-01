import urllib.request, urllib.parse, urllib.error
import json


serviceurl = 'http://py4e-data.dr-chuck.net/comments_11339.json'

connection = urllib.request.urlopen(serviceurl)

data = connection.read().decode()

try:
    info = json.loads(data)
except:
    info = None

if not info :
    print ('Data Retrieving Failure....')

print('Comment count:', len(info))

total = sum(item['count'] for item in info['comments'])

print (total)
