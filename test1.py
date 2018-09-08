import re
from urllib.request import Request , urlopen

url = "https://www.google.com/search?q="
url1 = "&tbm=fin"

stock = input("Enter the stock name ")

url = url + stock + url1
print ("<"+url+">")
req = Request(url)
data = urlopen(req).read()
data1 = data.decode("utf-8")
print(data1)