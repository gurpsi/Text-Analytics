#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 13:45:40 2017
Program to Tokenize and to Normalise

@author: gurpreetsingh

Normailzation.

"""


import nltk
temp= open('/Users/gurpreetsingh/Desktop/test.txt')
rawtext=temp.read()
print("Raw Text \n", rawtext,"\n")
tokens=nltk.word_tokenize(rawtext)
print ("Tokens: \n", tokens,"\n")
token=str(tokens) #SInce lower is applicable only to Strings.
low_token= token.lower() # To Make all the text in to lower characters.
print ("All tokens in lower case: \n", low_token,"\n")
punctuation=" . ? @ ! # $ % ^ & * ( ) ' " #Defining the punctuation
for p in punctuation:
    punc_free=low_token.replace(p,' ') #replacing punctuation to spaces
print (" The text after Normilisation: \n",punc_free)