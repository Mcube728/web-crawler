from mushroom_soup import *
import time
from info_log import *
from error_log import *
import requests
import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import json
import urllib.robotparser as urobot

def run(toVisit,  crawled):
    infoLogger('')
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
            errorLogger(f'This is the title:{title}')
            return
        json = returnJSON(title, description, url)
        print(f'JSON: {json}')
        updateJSON(json)
    except Exception as e:
        errorLogger(f'URL: {url} | {e}')

def getAnchors(url,s):
    infoLogger('getAnchors() called')
    for link in s.find_all('a'):
        if link.get('href') is not None:
            a = link.get('href')
            if a.startswith('/'):
                a = urljoin(url,a)
            yield a

def updateJSON(json_data, path='./data_export/results.json'):
    infoLogger('updateJSON() called')
    if not os.path.isfile(path):
        empty = json.dumps({'Links': []}, indent=4)
        fileMaker(path, empty)
        infoLogger('Json file created')
    with open(path, 'r+') as file:
        data = json.load(file)
        data['Links'].append(json_data)
        file.seek(0)
        json.dump(data, file, indent=4)
        infoLogger('results.json has been updated')                

def returnJSON(title, desc, url):
    json = {
        'Title': title,
        'Description': desc,
        'URL': url
    }
    return json