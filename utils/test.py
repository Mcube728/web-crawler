import spider

toVisit = {'https://www.nationalgeographic.com/'}
crawled = set()

spider.run(toVisit, crawled)