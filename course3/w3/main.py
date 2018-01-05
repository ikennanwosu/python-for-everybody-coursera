import urllib
import re

fname = "http://py4e-data.dr-chuck.net/regex_sum_56359.txt"
datasource = urllib.urlopen(fname)
line = datasource.readline()
total_sum = 0
while line != "":
	number_sum_in_this_line = sum(map(int, re.findall('[0-9]+', line)))
	total_sum += number_sum_in_this_line
	line = datasource.readline()

print(total_sum)
