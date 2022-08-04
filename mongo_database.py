from pymongo import MongoClient




class StoreMongo:
    def __init__(self,collection):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['financialnews']
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
            print(doc['article'])
            article = article + doc['article']
        return article
        # return article

