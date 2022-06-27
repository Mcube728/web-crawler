import utils.spider as spider

toVisit = {input("What webpage do you want me to start from?: ")}
print(type(toVisit))
crawled = set()

spider.run(toVisit, crawled)