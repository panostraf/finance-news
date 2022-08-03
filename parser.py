import requests
from bs4 import BeautifulSoup


class GetRecentArticles:
    BASE_URL = """https://www.investing.com/news/commodities-news"""
    pages = 4
    
    def extract_article(self,content_):
        '''
        Inpur <str> page source code from investing.com spesific article
        Returs <str> article
        '''
        cont_soup = BeautifulSoup(content_,parser='lxml',features="lxml")
        paragraphs = cont_soup.findAll('p')
        article = ""
        for p in paragraphs[2:-20]:
            article += f" {p.text}"
        return article

    def extract_article_info(self,content_):
        cont_soup = BeautifulSoup(content_,parser='lxml',features="lxml")
        date = cont_soup.findAll('div',class_='contentSectionDetails')
        title = cont_soup.findAll('h1',class_='articleHeader')
        print(cont_soup.findAll('h1'))
        return date, title

    def extract_links(self,page):
        '''
        Input <str> page source code from investing.com news
        Returns generator function with all the links for commodities
        '''
        soup = BeautifulSoup(page,parser='lxml',features="lxml")
            
        articles = soup.find_all('article')
        for article in articles:
            article = article.find_all('a')
            if len(article) > 1:
                article_link = article[1].get('href')
                article_link = self.validate_urls(article_link)
                if article_link:
                    yield article_link
                

    def validate_urls(self,url):
        '''
        validates that a url refers to commodities
        '''
        url = url.split("/")
        if "commodities-news" in url:
            return  self.BASE_URL + url[-1]
        return None

    
    
if __name__=='__main__':
    # PAGE = "PAGE CONTENT AS STRING FROM HTML"
    # scrapper = GetRecentArticles()
    # links = scrapper.extract_links(PAGE)
    # articles = [scrapper.extract_article(link) for link in links]

    article = open('test.html').read()
    scrapper = GetRecentArticles()
    title,date = scrapper.extract_article_info(article)
    print(date)
    print(article)