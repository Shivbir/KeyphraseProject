'''
Created on Sep 5, 2014

@author: randall
'''

import nltk
import pygraph

#63382



f = open("63382.txt")
raw = f.read()
sentences = nltk.sent_tokenize(raw)
#words = []
#print(tokens)
#print(nltk.word_tokenize("Witnesses, which simply record the status of the file but contain no data, can be used in addition to or in place of files to reduce overhead."))
print(nltk.pos_tag(nltk.word_tokenize("Witnesses, which simply record the status of the file but contain no data, can be used in addition to or in place of files to reduce overhead.")))

# Frequency, takes a word and a document
def f(w, d):
    #cant finish writing until i know what a document object looks like
    return 666