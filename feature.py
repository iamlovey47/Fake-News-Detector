import numpy as np # linear algebra
import pandas as pd #data processing
from nltk.stem import WordNetLemmatizer

from nltk.tokenize import RegexpTokenizer



import os
import re
import nltk
# nltk.download('stopwords')

def get_all_query(title, text):
    total= title + text
    totalString=total
    total = [total]
    return total

def remove_punctuation_stopwords_lemma(sentence):
    # filter_sentence = ''
    # lemmatizer=WordNetLemmatizer()
    # s=row[sentence]
    # s = re.sub(r'[^\w\s]','',s)
  

    # tokenizer = RegexpTokenizer(r'\w+')
    # s=tokenizer.tokenize(sentence)

    words = nltk.word_tokenize(sentence) #tokenization
    words = [w for w in words if not w in stop_words]
    for word in words:
        filter_sentence = filter_sentence + ' ' + str(lemmatizer.lemmatize(word)).lower()
    return filter_sentence

    