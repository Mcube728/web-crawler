# Web Crawler

A simple webcrawler written in python to discover content on the web. 

## Features: 
* Given a starting URL, it will look for every anchor tag in the html file, and add them to the list of URLs to crawl. 
* Saves those links with a title in a JSON file

### Dependencies: 
* BeautifulSoup4
* Requests
* Urllib
* json

You can just install the requirements.txt using pip
```
pip install -r requirements.txt
```

## How does the crawler work?
The crawler is given a starting URL. It then obtains the html content of the page, and obtains certain metadata like title and description. Then it finds out each and every anchor tag contains has an href attribute, and adds it to a list of urls to visit. Once this is completed, the crawler adds the current url to the list of crawled websites. If the current url has a title, the URL, title and description(this can occasionally be empty) is then passed to a method which converts these to JSON format and saves this in a file. 

Actual output from the json file(in our case -> results.json)
```
{
    "Links": [
        {
            "Title": "DMOZ - The Directory of the Web",
            "Description": "Expand the largest, most comprehensive, human-reviewed directory of the web",
            "URL": "https://www.dmoz-odp.org/docs/en/cmbuild.html"
        },
        {
            "Title": "DMOZ - Shopping: Food",
            "Description": "Websites which sell food and food products online are listed here.",
            "URL": "https://www.dmoz-odp.org/docs/en/cmbuild.html"
        },
        {
            "Title": "DMOZ - World: Dansk: Netbutikker: Mad og drikke",
            "Description": "Denne kategori indeholder dansksprogede web-steder, der handler om onlinesalg af mad og drikke.",
            "URL": "https://www.dmoz-odp.org/docs/en/cmbuild.html"
        }
    ]
}
```