import pymongo
from pymongo import MongoClient


class MongoDB:
    def __init__(self,collection=None):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['financialnews']

        if collection:
            self.collection = self.db[collection]
            
    def getAllArticles(self):
        '''
        Generator:
        reads all articles from a database and yields articles

        Saves memory since it is not going to store all documents in a list
        '''
        db = self.db

        # Loop over all collections
        for coll in db.list_collection_names():
            self.collection = self.db[coll]

            # Query using this collection and read all articles
            docs = self.collection.find({},{'article':1,"_id":0})
            
            # yield all articles
            for doc in docs:
                yield doc






if __name__=='__main__':
    mdb = MongoDB()
    for a in mdb.getAllArticles():
        print(a['article'])
        print('=======\n\n')