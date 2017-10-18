temp=open("/Users/gurpreetsingh/Desktop/test1.txt")
raw_text=temp.read()
print("Here is the raw text: \n\n", raw_text,"\n")
word_count=len(raw_text.split())
print("Total number of words in file is: ",word_count,"\n")
split_raw_text=raw_text.split(" ")
print("Here is the raw text after splitting: \n\n",split_raw_text,"\n")
from nltk.stem import PorterStemmer
print([PorterStemmer().stem(words) for words in split_raw_text])

'''
Here the words of the file are getting stemmed out by using PorterStemmer 
'''