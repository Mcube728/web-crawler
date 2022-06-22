'''
this is just a tester file to see if things work
'''
from urllib.error import HTTPError
import requests
from bs4 import BeautifulSoup
import ssl
import urllib.robotparser as urobot

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url="https://www.4chan.org/"
#url="http://docs.python-requests.org/en/latest/user/quickstart/#response-status-codes"

r = requests.get(url)
html = r.text
print(html)

s = BeautifulSoup(html, 'html.parser')
for link in s.find_all('a'):
    print('found a link')
s = {"this", 'is', 'a', 'file'}
for i in s:
    print(i)