# Installation
Clone repo
Create a virtual environment and install dependencies
<pip install -r requirements.txt>

Download and instaall mongo db
(let it run on the default settings: < mongodb://localhost:27017/ >)

Since it uses selenium under chromedriver, please download and save the executable in the root directory
(You can download it from here:
https://chromedriver.storage.googleapis.com/index.html?path=103.0.5060.134/
)


# Usage
cd to root directory
activate virtual environment: 
 - [source venv/bin/activate] for mac users
 - [venv\Scripts\activate]    for windows users

 Start mongodb server

 Then you can execute crawler.py along with the category you want to download
 The articles will be stored in the MongoDB under financialnews database to the corresponding collection

 e.g.
 python crawler.py economy
 python crawler.py stocks


 When you have populate the collection you can create wordcloud for a given category
 Execute news_insights.py to create a wordcloud
 e.g.
 python news_insights.py economy
 python news_insights.py stocks


# Available categories
- commodities
- stocks
- forex
- economy
- politics
- economic indicators

