# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 15:42:27 2017

@author: adam harris
"""
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# nltk.download()  # download all if nltk is not already installed.

# tokenizing - word tokens, chopping a document up into individual words or sentence tokens is chopping up into sentences
# lexicon - is the vocabulary of a person e.g. stokebroker or medical doctor.  Can also be vocabulary of a language e.g.American English
# corpora - is a body of text e.g. journals, blog post, news article
# 

example_text = "Tokenizing, even in English, is a difficult problem. It's even harder in other languages - such as Chinese!"

# Activity 1 - Tokenizing
# tokenizing example text, print out each token
for word in word_tokenize(example_text):
    print (word)
    
# Activity 2 - StopWord Removal    
# removal of 'english' stop words from the example text.  NLTK has a number of pre-defined stopword lists like english etc
stop_words = set(stopwords.words("english"))

# creating tokens from example text
tokens = word_tokenize(example_text)

tokens_noStopWords = []  # empty array to store tokens with stop words removed

# loop through tokens and only save the tokens are not in stopword list
for t in tokens:
    if t not in stop_words:
        tokens_noStopWords.append(t)
        
print (tokens_noStopWords)

# Activity 3 - Stemming    
# Stemming is merging words of similar origin and meaning.  e.g. minimise, minimal, minimum in to single token
ps = PorterStemmer()
example_text2 = ["hypothetically","destructiveness","adjustment"]