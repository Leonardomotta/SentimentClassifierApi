import pickle
from  sklearn import tree
from ScrapTweets.scrap import GetTweetsByYear
from sklearn.feature_extraction.text import CountVectorizer
from DataCleaner.dataCleaner import cleanText
import pandas as pd
import firebase_admin
from firebase_admin import db
import requests 
import json 


with open('./pickleFiles/classificador.pickle', 'rb') as f:
    clf = pickle.load(f)

with open('./pickleFiles/cv.pickle', 'rb') as a:
    cv = pickle.load(a)


url = "https://sentimentclassifier-60574-default-rtdb.firebaseio.com"


def predict(candidato,ano) :
  
  tweets_cl = []
  polaridade = []
  timestamp = []
  tweets = []

  dados = requests.get("{url}/{candidato}/{ano}.json".format(url=url,candidato=candidato,ano = ano))
  dados = dados.json()
    
  if dados is None :
        tweets_df2 = GetTweetsByYear(candidato,ano)
        
        for i in tweets_df2['Text'].to_numpy() :
            tweets_cl.append(cleanText(i)) 
            tweets.append(str(i)) 
        
        for j in tweets_df2['Datetime'].to_numpy() :
            timestamp.append(str(j)) 
            
        xtvec = cv.transform(tweets_cl).toarray()
        y_pred = clf.predict(xtvec)

        positivos = 0 
        negativos = 0
        neutro    = 0

        for i in y_pred :
            
            if i == 1 :
                positivos += 1

            elif i == 0 :
                neutro += 1
            else :
                negativos += 1

            polaridade.append(int(i))
            

        dados ={"tweets" : tweets,
        "polaridade" : polaridade,
        "timestamp" : timestamp,
        "positivos" : positivos,
        "negativos" : negativos,
        "neutro" : neutro,
        "total" :  len(tweets)}

        req =  requests.post("{url}/{candidato}/{ano}.json".format(url=url,candidato=candidato,ano = ano) ,data=json.dumps(dados))      
      
      
      
      
  
  return dados