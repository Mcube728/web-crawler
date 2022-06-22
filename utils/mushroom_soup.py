import os

def file_writer(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def make_data_files(url):
    queue = os.getcwd() + '/data_export/queue.txt'
    crawled = os.getcwd() + '/data_export/crawled.txt'
    if not os.path.isfile(queue):
        file_writer(queue,url)
    if not os.path.isfile(crawled):
        file_writer(crawled,'')

def append_content_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

def clear_file_contents(path):
    with open(path, 'w'):
        pass

def to_set(fileName):
    results = set()
    with open(fileName, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

def to_file(links, file):
    clear_file_contents(file)
    for link in links: 
        append_content_to_file(file, link)

print(os.getcwd())