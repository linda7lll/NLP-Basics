# -*- coding: utf-8 -*-
"""
Created on Sun May  2 13:39:06 2021

@author: Linda
"""
#gTTS(Google Text-to-Speech)

from gtts import gTTS
import os #işletim sistemindeki dosyalara erişim için 


gTTS(text = "Bugün yapay zekanın kötü bir süper zeka olmasından endişelenmek, Mars’taki aşırı nüfus artışından endişelenmek gibidir.", lang = "tr", slow = False).save("text.mp3")
os.system("start text.mp3")



