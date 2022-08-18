import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
import pickle
import re

with open('./pickleFiles/stopwords.pickle', 'rb') as f:
    stopwords = pickle.load(f)

ps = PorterStemmer()




def cleanText(text) :
    text = re.sub('@[A-Za-z0-9]+','',text) #remove menções
    text = re.sub('https?:\/\/\S+','',text)#remove links 
    text = re.sub('RT[\s]+','',text)
    text = re.sub("http\S+", "", text)
    text = re.sub("www.\S+", "", text)
    text = re.sub('[()!?]', ' ', text)
    text = re.sub('\[.*?\]',' ', text)
    
    
    text =  text.lower()
    
    #tokenize
    tokenizer = RegexpTokenizer('\w+')
    tokens = tokenizer.tokenize(text)
    clean_tokens =  [token for token in tokens if token not in stopwords]
    stemmed_tokens = [ps.stem(token) for token in clean_tokens]
    clean_text = " ".join(stemmed_tokens)
    

    return clean_text