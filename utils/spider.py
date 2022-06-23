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

def getHTML(url):
    info_logger('getHTML() called')
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
    info_logger(f'getHTML() ran successfully and obtained the content from {url}')
    return r.text

def crawl(url):
    info_logger('crawl() called')
    visited = []
    toVisit = []
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')
    info_logger(f'Now crawling ==> {soup.title.text}:{url}')
    visited.append(url)
    fileWriter('./data_export/visited_links.txt', soup.title.text + ": " + url + "\n")
    toVisit.extend(getAnchors(soup,url))



def fileWriter(path, data):
    f = open(path, 'a')
    f.write(data)
    f.close()

def getAnchors(soup, url):
    info_logger('getAnchors() called')
    anchors = []
    for link in soup.find_all('a'):
        if link.get('href').startswith('/'):
            path = urljoin(url, link.get('href'))
            anchors.append(path) # put relative links
            continue
        anchors.append(link.get('href')) # put absolute links
    anchors = list(set(anchors))
    for a in anchors: 
        fileWriter('./data_export/queued_links.txt', a + "\n")
    info_logger(f'getAnchors() ran successfully and obtained {len(anchors)} links')
    return anchors

url = 'https://reddit.com'
crawl(url)