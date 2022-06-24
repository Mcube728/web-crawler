import os

def fileMaker(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def makeDataFiles(url):
    queue = './data_export/queue.txt'
    crawled = './data_export/crawled.txt'
    if not os.path.isfile(queue):
        fileMaker(queue,url)
    if not os.path.isfile(crawled):
        fileMaker(crawled,'')

def appendContentToFile(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

def clearFileContents(path):
    with open(path, 'w'):
        pass

def toList(fileName):
    results = []
    with open(fileName, 'rt') as f:
        for line in f:
            results.append(line.replace('\n', ''))
    return results

def toFile(links, file):
    clearFileContents(file)
    for link in links: 
        appendContentToFile(file, link)


print(os.getcwd())