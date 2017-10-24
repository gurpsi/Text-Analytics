
import nltk
import string
temp= open('/Users/gurpreetsingh/Desktop/test.txt')
rawtext=temp.read()

word_count=len(rawtext.split())
print("Total number of words in the file are: ", word_count, "\n")
print("Here is the raw text of the file:  \n", rawtext,"\n")
tokens=nltk.word_tokenize(rawtext)
print ("These are the tokens from that file: \n", tokens,"\n")



token=str(tokens)   #Since lower() function is applicable only to Strings.
low_token= token.lower()    # To Make all the text in to lower characters.
print ("All tokens in lower case: \n", low_token,"\n")
exclude= set(string.punctuation)    # punctuation is not a function, but just an attribute (variable) of string module that holds all punctuation characters.
print("These are excluded from the text: \n", exclude,"\n")
punc_free="".join(ch for ch in low_token if ch not in exclude)
print (" The text after Normalisation: \n",punc_free,"\n")


tokens_punc_free=nltk.word_tokenize(punc_free)      #Re-tokenizing as the 'pos_tag' accepts only Tokens.
print("Re-tokenized: \n", tokens_punc_free,"\n")
pos_tokens=nltk.pos_tag(tokens_punc_free)
print ("Data after POS Tagging: \n",pos_tokens)