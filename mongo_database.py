from pymongo import MongoClient
import re
from helpers import helpers


class StoreMongo:
    def __init__(self,collection=None):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['financialnews']
        print(collection,"--")
        if collection:
            self.collection = self.db[collection]
        
        

    def insert_values(self,article,date,title):
        post = {
                'title':title,
                'date':date,
                'article':article,        
        }
        self.collection.insert_one(post)

    def mergeAllArticles(self):
        docs = self.collection.find({},{'article':1,"_id":0})
        article = ""
        for doc in docs:
            # print(doc['article'])
            article = article + doc['article']
        for t in self.collection.find({},{'title':1,"_id":0}):
            print(t)
        return article
        # return article
    
    def all_collections(self):
        db = self.db
        article = ""
        for coll in db.list_collection_names():
            self.collection = self.db[coll]
            article = article + self.mergeAllArticles()
        return article

    def get_dates(self):
        docs = self.collection.find({},{'date':1,"_id":0})
        for d in docs:
            # print(d)

            found = re.search('[A-Za-z]{3}\s[0-9]{2},\s[0-9]{4}',str(d))
            # print(found[0])
            print('---',helpers.convert_date(found[0]))

if __name__=='__main__':
    sm = StoreMongo('politics')
    sm.get_dates()