from selenium import webdriver
from bs4 import BeautifulSoup
import time
from parser import GetRecentArticles
from collections import defaultdict
from urllib3 import exceptions as exc
import random
from helpers import helpers
from mongo_database import StoreMongo
import sys
import settings

# scrapped_articles = []
# BASE_URL = """https://www.investing.com/news/commodities-news/"""

class Crawler:
    ''' initialize Chrome drivers - headless (not showing google chrome)'''
    
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    op.add_argument('--incognito')
    driver = webdriver.Chrome('./chromedriver',options=op)
    
    
    def __init__(self,url):
        '''Initialize url'''
        self.url = url
        # self.url = """https://www.investing.com/news/commodities-news/3"""
    
    def get_page(self):
        '''
        makes request using selenium package and returns html page source code <str>
        If not content available returns None
        '''
        try:
            self.driver.get(self.url)
            content = self.driver.page_source
            return content
        except Exception as E:
            print("Couldn't fetch", self.url)
            print(E)
        return



def main(url,collection):
    crawler = Crawler(url) #initialize crawler class
    time.sleep(10)
    content = crawler.get_page() # extract content (to gather urls)
    parser = GetRecentArticles(url) # Initialize parser class
    links = parser.extract_links(content) # Extract list of articles (urls)
    sm = StoreMongo(collection)

    if not links:
        return
    # visit each article and parse it's content
    for link in links:
        crawler.url = link
        article_content = crawler.get_page()
        if not article_content:
            continue
        print(link)
        # clean text of the article page (only <p> tags )
        article = parser.extract_article(article_content) 

        try:
            # extract date and title of the article
            date, title = parser.extract_article_info(article_content)
            
        except:
            print("date and title not found")
            date,title = "NA","NA"
        # date, title = parser.extract_article_info(article_content)

        sm.insert_values(article,date,title)
        sleep_time = random.randint(1,6)
        time.sleep(sleep_time)

    crawler.driver.quit()

if __name__=='__main__':
    category = sys.argv[1]
    url = settings.collections[category]['BASE_URL']
    collection = settings.collections[category]['collection']
    main(url,collection)
