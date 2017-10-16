#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 21:05:57 2017

@author: gurpreetsingh

Tokenization -> Normalization -> pos tagging
"""

import nltk
import string
temp= open('/Users/gurpreetsingh/Desktop/test.txt')
rawtext=temp.read()
print("Raw Text: \n", rawtext,"\n")
tokens=nltk.word_tokenize(rawtext)
print ("Tokens: \n", tokens,"\n")
token=str(tokens) #Since lower is applicable only to String.
low_token= token.lower() # To Make all the text in to lower characters.
print ("All tokens in lower case: \n", low_token,"\n")
exclude= set(string.punctuation) # This is the set of punctuations I am removing 
print("These are excluded from the text: \n", exclude,"\n")
punc_free="".join(ch for ch in low_token if ch not in exclude)
print (" The text after Normilisation: \n",punc_free,"\n")
tokens_punc_free=nltk.word_tokenize(punc_free)
print("Re-tokenized: \n", tokens_punc_free,"\n")
pos_tokens=nltk.pos_tag(tokens_punc_free)
print ("Data after POS Tagging: \n",pos_tokens,"\n")