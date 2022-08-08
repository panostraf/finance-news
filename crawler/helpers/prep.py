import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

import re


class ArticlePreprocessing:
    lemma = WordNetLemmatizer()
    stemmer = SnowballStemmer("english")


    stops = [
        'said',
        'month','week','year','day',
        'january','february','march','may','jun','july','august','september','octomber','november','december'
        'monday','thursday','tuesday', 'wednesday','friday'
    ]
    stpw = stopwords.words('english')
    stpw.extend(stops)


    def clean_tokens(self,text):#article_path='data/articles/article1'):
        # text = open(article_path).read()
        tokens = nltk.word_tokenize(text)


        tokens = [self.lemma.lemmatize(token) for token in tokens]
        tokens = [token.lower() for token in tokens if tokens not in self.stpw]
        tokens = [self.clean_words(token,self.stpw) for token in tokens if token != "None"]
        tokens = [token for token in tokens if token is not None]

        c_tokens = []
        for token in tokens:
            if token is not None:
                c_tokens.append(token)

        return c_tokens

    @staticmethod
    def tokens_to_doc(tokens):
        text = ' '.join(tokens)
        return text

    @staticmethod
    def clean_words(word,custom_stops):
        if len(word) <3:
            return 
        if word in custom_stops:
            return 
        word = re.sub(r'[^a-zA-Z]', '', word)
        return word
