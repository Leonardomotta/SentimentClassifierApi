import snscrape.modules.twitter as sntwitter
import snscrape.modules.twitter as sntwitter
import pandas as pd


tweets_list2 = []

def GetTweetsByYear(term,year) :

    tweets_list2 = []

    for i in range (1,13):
        query = "{term} since:{year}-{month}-1 until:{year}-{month}-15 lang:pt".format(term = term, year = year, month = i) 
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
            if i>1000:
                break
            tweets_list2.append([tweet.date, tweet.id, tweet.content])
    
    return pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text'])
   


