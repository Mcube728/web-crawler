from mushroom_soup import *
from time import asctime
from info_log import *
from error_log import *
import requests
import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import queue
from pathlib import Path
import urllib.robotparser as urobot

def run(toVisit):
    for link in toVisit:
        crawl(link)

def crawl(url):
    info_logger('crawl() method called')
    visited = []
    toVisit = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
    try: 
        r = requests.get(url, headers=headers)
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        error_logger(f'Bad Status code: {r.status_code}')
    except requests.exceptions.ConnectionError as errc:
        error_logger(f'Error Connecting to {url}')
    except requests.exceptions.Timeout as errt:
        error_logger('Timeout Error connecting to {url}')
    except requests.exceptions.RequestException as err:
        error_logger('An Error Occurred')
    info_logger(f'Status code of request set to {url}: {r.status_code}')
    soup = BeautifulSoup(r.text, 'html.parser')
    info_logger(f'Now crawling ==> {soup.title.text}:{url}')
    visited.append(url)
    fileWriter('./data_export/visited_links.txt', soup.title.text + ": " + url + "\n")

def fileWriter(path, data):
    f = open(path, 'a')
    f.write(data)
    f.close()

def getAnchors(soup, url):
    info_logger('getAnchors() called')
    anchors = []
    for link in soup.find_all('a'):
        #info_logger('An interation started')
        if link.get('href').startswith('/'):
            #info_logger('if got called')
            path = urljoin(url, link.get('href'))
            anchors.append(path) # put relative links
            #info_logger(f'{path} got added to anchors')
            continue
        #info_logger('if you see this, something\'s wrong.')
        anchors.append(link.get('href')) # put absolute links
        #info_logger(f"{link.get('href')} got added to anchors")
    anchors = list(set(anchors))
    info_logger('getAnchors() ran successfully')
    return anchors

url = 'https://reddit.com'
crawl(url)