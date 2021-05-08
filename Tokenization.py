# -*- coding: utf-8 -*-
"""
Created on Sun May  9 01:00:04 2021

@author: Linda
"""
#nltk kutuphanesini kullanarak cumle ve kelime tokenize etme islemleri

import nltk    
from nltk import sent_tokenize

#sentence tokenization/cümle tokenize etme

text = "İnsanda ümitsizliğin bir derecesi vardır ki, o vakit irade sevkitabii gibi kördür. Nasılsız ve nicesizdir, gayesinde sarhoş gibi körkütük gider ve o vakit insiyaki bir iş gören zeka, ne yaptığını bilmez. Peyami Safa (Server Bedi)"
sentences = sent_tokenize(text)
for sentence in sentences:
    print(sentence)
    
    
#%%    
 
#word tokenization/kelime tokenize etme

import nltk    
from nltk import word_tokenize
text = ["bir avuntu, biraz keder."]
sentences = word_tokenize(text)
for sentence in sentences:
    print(sentence)
    


    
