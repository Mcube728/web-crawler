# Web Crawler

A simple webcrawler written in python to discover content on the web. 

## Features: 
* Given a starting URL, it will look for every anchor tag in the html file, and add them to the list of URLs to crawl. 
* Saves those links with a title in JSON format(work in progress, still implementing this!)

###Dependencies: 
* BeautifulSoup4
* Requests
* Urllib

You can just install the requirements.txt using pip
```
pip install -r requirements.txt
```