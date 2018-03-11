#This program learn to compare between male and females, on providing the test data. (Supervised learning)
#And we compare the accuracy for the old function vs the modified function.

import nltk
from nltk.corpus import names
import random

def gender_features(word):
    return {'last_letter': word[-1]}

vowel=['A','E','I','O','U','a','e','i','o','u']
def modified_gender_features(word):
    return { 'first-letter': word[0], 'first-last letter':word[0] + word[-1],
             'word length': len(word) < 5, 'last-word-vowel': word[-1] in vowel}

male_names = [(name, 'male') for name in names.words('male.txt')]
print(male_names)
female_names = [(name, 'female') for name in names.words('female.txt')]
print(female_names)
labeled_names = male_names + female_names
random.shuffle(labeled_names)
featuresets_old = [(gender_features(n), gender) for (n, gender) in labeled_names]
featuresets_new = [(modified_gender_features(n), gender) for (n,gender) in labeled_names]

train_set_old, test_set_old = featuresets_old[500:], featuresets_old[:500]
train_set_new, test_set_new = featuresets_new[500:], featuresets_new[:500]


classifier_old = nltk.NaiveBayesClassifier.train(train_set_old)
classifier_new = nltk.NaiveBayesClassifier.train(train_set_new)

ans1 = classifier_old.classify(gender_features('Mark'))
ans2 = classifier_old.classify(gender_features('Precilla'))
ans3 = classifier_new.classify(modified_gender_features('Mark'))
ans4 = classifier_new.classify(modified_gender_features('Precilla'))

print("Old function: \n \t Mark is:", ans1)
print(" \t Precilla is:", ans2)
print("As per New function: \n \t Mark is:", ans3)
print(" \t Precilla is:", ans4)

classifier_old.show_most_informative_features(5)
classifier_new.show_most_informative_features(5)

print(nltk.classify.accuracy(classifier_old, test_set_old))
print(nltk.classify.accuracy(classifier_new, test_set_new))
