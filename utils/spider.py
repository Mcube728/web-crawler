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
    '''
    A method that runs the crawler if there are links in 
    the waiting set. 

    Parameters:
        toVisit(set): The set of links that need to be crawled
        crawled(set): The set of links that have been crawled
    '''
    infoLogger('')
    infoLogger('run() method called')
    while toVisit: 
        url =  toVisit.pop()
        infoLogger(f'{url} got removed from the queue')
        crawl(url, toVisit, crawled)

def crawl(url, toVisit, crawled):
    '''
    This method makes a get request to the specified url
    and obtains that page's html source code, along with 
    metadata like the page's title and description, if any. 

    Parameters:
        url(str): The url that the crawler needs to visit
        toVisit(set): The set of links that need to be crawled
        crawled(set): The set of links that have been crawled
    '''
    infoLogger(f'crawl() method called; url = {url}')
    print(f'Queued Links: {len(toVisit)} | Crawled Links: {len(crawled)}')
    try:
        title, description = 'na'
        r = requests.get(url)
        infoLogger(f'Status: {r.status_code}')
        s = BeautifulSoup(r.text, 'html.parser')
        title = s.title.text
        description = s.find('meta', {'name':'description'}).get('content')
        for url in getAnchors(url,s):
            toVisit.add(url)
        crawled.add(url)
        if title == 'na':
            errorLogger(f'This is the title:{title}')
            return
        updateJSON(returnJSON(title, description, url))
    except Exception as e:
        errorLogger(f'URL: {url} | {e}')

def getAnchors(url,s):
    '''
    This function takes the url and the soup object from
    the crawl function and finds out all the anchor tags 
    that contain an href attribute present in the html code.  

    Parameters:
        url(str): The url that the crawler has visited
        s('bs4.BeautifulSoup'): The BeautifulSoup object
    '''
    infoLogger('getAnchors() called')
    for link in s.find_all('a'):
        if link.get('href') is not None:
            a = link.get('href')
            if a.startswith('/'):
                a = urljoin(url,a)
            yield a

def updateJSON(json_data, path='./data_export/results.json'):
    '''
    This function checks if there is a JSON file to save 
    the results in. If there is no JSON file, it is created
    with an empty dictionary. If the file exists, the data 
    is loaded and the JSON data for the link is appended to
    the JSON file. 

    Parameters: 
        json_data('dict'): The dictionary that contains the title, description and url of the visited page
        path(str): The path to save the JSON file   
    '''
    infoLogger('updateJSON() called')
    if not os.path.isfile(path):
        empty = json.dumps({'Links': []}, indent=4)
        fileMaker(path, empty)
        infoLogger('Json file created')
    with open(path, 'r+') as file:
        data = json.load(file)
        data['Links'].append(json_data)
        file.seek(0)    # Change file position to the start, so that another dictionary is not written to the json file. 
        json.dump(data, file, indent=4)
        infoLogger('results.json has been updated') 
        file.close()               

def returnJSON(title, desc, url):
    '''
    This function takes the title, description and the url 
    and saves them in a dictionary so that they can be saved
    in the json file for the crawled links.  
    '''
    json = {
        'Title': title,
        'Description': desc,
        'URL': url
    }
    return json