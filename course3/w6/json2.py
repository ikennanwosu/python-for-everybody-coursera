import json
import urllib.request

url = input("Enter location: ")
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_42.json"


data = urllib.request.urlopen(url).read().decode()
info = json.loads(data)["comments"]
print('comments count:', len(info))

total = 0
for item in info:
    total += int(item['count'])

print(total)
