# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
ans = 'Kyleena'
new_url = ''

for time in range(count):
	position_i = 0
	if time != 0:
    	# go to the current link
		html = urllib.request.urlopen(new_url, context=ctx).read()
		soup = BeautifulSoup(html, 'html.parser')

		# Retrieve all of the anchor tags
		tags = soup('a')
	for tag in tags:
	    new_url = tag.get('href', None)
	    ans = tag.contents[0]
	    position_i += 1
	    if position_i == position:
	    	break

print(ans)