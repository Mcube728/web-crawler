import spider

toVisit = {'https://www.dmoz-odp.org/'}
crawled = set()

spider.run(toVisit, crawled)