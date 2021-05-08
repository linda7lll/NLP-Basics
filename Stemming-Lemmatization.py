# -*- coding: utf-8 -*-
"""
Created on Sun May  9 01:33:36 2021

@author: Linda
"""

#1)stemming(gövdeleme) 

import nltk
from nltk.stem.porter import *
Porter_Stemmer = PorterStemmer()

input1 = "classifications"
print(Porter_Stemmer.stem(input1)) #output: classif

#%%

#tüm diller için snowballstemmer kutuphanesi
import nltk
from snowballstemmer import TurkishStemmer

turk_stemmer = TurkishStemmer()
input2 = "kalemler"
print(turk_stemmer.stemWord(input2)) #output : kalem

input3 = "kalemlikler"
print(turk_stemmer.stemWord(input3)) #output : kalemlik

#%%


#2)lemmatization(baş sözcük çıkarma)
import spacy
nlp = spacy.load('en_core_web_sm')
input4 = nlp('classifications')
for token in input4:
    print(token.lemma_)
    
#%%    
    
  

