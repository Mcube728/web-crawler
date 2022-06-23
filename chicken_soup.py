'''
this is just a scratchpad python file that is 
used to test out a few things, please do not 
mind this file. 
'''

import requests
import os
from utils.info_log import *
from utils.error_log import error_logger
from utils.mushroom_soup import *
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url="https://www.reddit.com"
#url="http://docs.python-requests.org/en/latest/user/quickstart/#response-status-codes"

r = requests.get(url)
print(f'Status of request sent to {url}: {r.status_code}')

s = BeautifulSoup(r.text, 'html.parser')
# s.find("title").text
# s.title.text
info_logger(f'Title of url: {s.find("title").text}')