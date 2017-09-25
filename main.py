import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *
import pandas as pd


PROJECT_NAME = input('enter project name')
print("creating project" + "" +  PROJECT_NAME)
HOMEPAGE = input('enter the address of homepage')
print("crawling to homepage of" + "" +  PROJECT_NAME)
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.csv'
CRAWLED_FILE = PROJECT_NAME + '/crawled.csv'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()



def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()



def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()



def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()

def merge():
   # filenames = [spider.crawled]
    with open('stopwords.csv', 'a') as outfile:
         with open(CRAWLED_FILE) as infile:
              for line in infile:
                  outfile.write(line)

def index(fileName):

    inFile=open(fileName,'r')
    index={}
    for line in inFile:
        line=line.strip()      #This will get rid of my new line character
        word=line[1]
        if word not in index:
            index[word]=[]
            index[word].append(line)
    return index
def readcsv(filename):
    #filename = open('stopwords.csv' , a)
    pd.read_csv(filename , header='none')






create_workers()
crawl()
merge()
index('stopwords.txt')