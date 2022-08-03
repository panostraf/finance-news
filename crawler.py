from selenium import webdriver
from bs4 import BeautifulSoup
import time
from parser import GetRecentArticles
from collections import defaultdict
from urllib3 import exceptions as exc
import random
from helpers import helpers

scrapped_articles = []


class Crawler:
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome('./chromedriver',options=op)
    
    def __init__(self,url):
        self.url = url
        # self.url = """https://www.investing.com/news/commodities-news/3"""
    
    def get_page(self):
        self.driver.get(self.url)
        content = self.driver.page_source
        return content

url = """https://www.investing.com/news/commodities-news/"""

def main(url):
    crawler = Crawler(url)
    content = crawler.get_page()
    parser = GetRecentArticles()
    links = parser.extract_links(content)
    
    # with open('articles3.txt' ,'a') as f: 
    #     for link in links:
    #         try:
    #             crawler.url = link
    #             article_content = crawler.get_page()
    #             article = parser.extract_article(article_content)
    #             f.write(str(article) + "\n\n")
    #             print(article)
    #         except exc:
    #             pass
    #         time.sleep(5)

    for link in links:
        try:
            crawler.url = link
            article_content = crawler.get_page()
            article = parser.extract_article(article_content)

            article_number = helpers.number_of_files() + 1
            artcl_name = f"article{str(article_number)}"

            with open(f'data/articles/{artcl_name}' ,'w') as f: 
                f.write(str(article) + "\n\n")
            f.close()

            # print(article)

        except:
            pass

        sleep_time = random.randint(1,6)
        time.sleep(sleep_time)

    crawler.driver.quit()


for i in range(1,5):
    print('page:',i)
    url = url + str(i)
    main(url)


quit()
exit(-1)

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome('./chromedriver',options=op)




url = """https://www.investing.com/news/commodities-news/3"""
driver.get(url)
content = driver.page_source

parser = GetRecentArticles()
links = parser.extract_links(content)

id = 0

with open('articles.txt','a') as f:
    for link in links:
        driver.get(link)
        article = parser.extract_article(driver.page_source)
        
        f.write(str(article)+',')
        time.sleep(3)
f.close()

# def extract_content(content_):
#     cont_soup = BeautifulSoup(content_)
#     paragraphs = cont_soup.findAll('p')
#     article = ""
#     for p in paragraphs[2:-20]:
#         article += f" {p.text}"
#     return article


# soup2 = BeautifulSoup(content)
# print(soup2)


time.sleep(20)

driver.quit()



