from mushroom_soup import *
import time
from info_log import *
from error_log import *
import requests
import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import queue
from pathlib import Path
import urllib.robotparser as urobot

def run(toVisit,  crawled):
    infoLogger('run() method called')
    while toVisit: 
        url =  toVisit.pop()
        infoLogger(f'{url} got removed from the queue')
        crawl(url, toVisit, crawled)

def crawl(url, toVisit, crawled):
    infoLogger(f'crawl() method called; url = {url}')
    print(f'Queued Links: {len(toVisit)} | Crawled Links: {len(crawled)}')
    try:
        title, description = 'na'
        r = requests.get(url)
        infoLogger(f'Status: {r.status_code}')
        s = BeautifulSoup(r.text, 'html.parser')
        #title = None
        title = s.title.text
        #description = None
        description = s.find('meta', {'name':'description'}).get('content')
        #print(f'Title: {title}')
        #print(f'Description: {description}')
        for url in getAnchors(url,s):
            toVisit.add(url)
        crawled.add(url)
        if title == 'na':
            return
        json = returnJSON(title, description, url)
        print(f'JSON: {json}')
    except Exception as e:
        errorLogger(e)

def getAnchors(url,s):
    infoLogger('getAnchors() called')
    for link in s.find_all('a'):
        if link.get('href') is not None:
            a = link.get('href')
            if a.startswith('/'):
                a = urljoin(url,a)
            yield a

def returnJSON(title, desc, url):
    json = {
        'Title': title,
        'Description': desc,
        'URL': url
    }
    return json

#toVisit = {'https://ocw.mit.edu/'}
#crawled = set()