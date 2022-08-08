from crawler import settings
from crawler.crawler import *

collections = list(settings.collections.keys())
# category = sys.argv[1]

for collection in collections:
    url = settings.collections[collection]['BASE_URL']
    collection = collection
    main(url,collection)