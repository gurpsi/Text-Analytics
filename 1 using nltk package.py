#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 13:20:20 2017

@author: gurpreetsingh

Question: Load the file in and use nltk.word_tokenizer() on it. Report the list of
tokens that are produced from it and note any oddities that arise.
Comment on these oddities and how they might be handled.
"""

import nltk
temp= open('/Users/gurpreetsingh/Desktop/test.txt')
rawtext=temp.read()
print(rawtext,"\n\n")
tokens=nltk.word_tokenize(rawtext)
print("Total words: \n", len(rawtext.split()),"\n")
print ("Tokens= \n",tokens)