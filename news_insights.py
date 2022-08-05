import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

import sys

from helpers import prep

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
# nltk.download('omw-1.4')





def create_word_cloud(text):
    wordcloud = WordCloud(width = 800, height = 800,
                        background_color ='white',
                        # stopwords = stopwords,
                        min_font_size = 10).generate(text)

    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    
    plt.show()

if __name__ == '__main__':
    news_collection = sys.argv[1]
    # file_path = 'data/articles/' + file_path
    import mongo_database

    # from pymongo import MongoClient
    if news_collection == 'all':
        se = mongo_database.StoreMongo()
        article = se.all_collections()
    else:
        se = mongo_database.StoreMongo(news_collection)
        article = se.mergeAllArticles()

    preprocessing = prep.ArticlePreprocessing()
    preprocessed_tokens = preprocessing.clean_tokens(text=article)
    preprocessed_text = preprocessing.tokens_to_doc(preprocessed_tokens)
    create_word_cloud(preprocessed_text)