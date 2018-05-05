#Name:          Samantha Garcia
#Section:       27F3
#Assignment:    EC1
#Due Date:      March 19th, 2018

import nltk
from nltk import *

#Chi-Square Test of Independence
def chi_square (word_one, word_two, corpus):
    word_list = []
    #Import the necessary corpus
    if corpus == "brown":
        from nltk.corpus import brown
        word_list = brown.words()
    elif corpus == "reuters":
        from nltk.corpus import reuters
        word_list = reuters.words()
    elif corpus == "gutenberg":
        from nltk.corpus import gutenberg
        word_list = gutenberg.words()
    elif corpus == "webtext":
        from nltk.corpus import webtext
        word_list = webtext.words()
    elif corpus == "inaugural":
        from nltk.corpus import inaugural
        word_list = inaugural.words()
    #Get the frequencies of each word
    w1 = word_list.count(word_one)
    w2 = word_list.count(word_two)
    #Get the frequencies of the word as a collocation
    bigrams = nltk.bigrams(word_list)
    freq_dist = nltk.FreqDist(bigrams)
    w1w2 = 0
    w1andnotw2 = 0
    notw1andw2 = 0
    notw1andnotw2 = 0
    total_words = len(word_list)
    for k, v in freq_dist:
        if k == word_one and v == word_two:
            w1w2 = w1w2 + 1
        elif k == word_one and v != word_two:
            w1andnotw2 = w1andnotw2 + 1
        elif k != word_one and v == word_two:
            notw1andw2 = notw1andw2 + 1
    notw1andnotw2 = notw1andw2 + w1andnotw2
    totalw1andw2 = w1w2 + w1andnotw2 + notw1andw2 + notw1andnotw2
    first_row = w1w2 + w1andnotw2
    second_row = notw1andw2 + notw1andnotw2
    first_col = w1w2 + notw1andw2
    second_col = w1andnotw2 + notw1andnotw2
    #Calculate chi-square value
    #Null hypothesis is that there is no collocation between the two words (no relationship)
    #Estimated value for each cell
    value_one = (first_row * first_col) / totalw1andw2
    value_two = (second_row * first_col) / totalw1andw2
    value_three = (first_row * second_col) / totalw1andw2
    value_four = (second_row * second_col) / totalw1andw2
    x2 = ((w1w2 - value_one) ** 2) / value_one
    x2 = x2 + ((w1andnotw2 - value_three) ** 2) / value_three
    x2 = x2 + ((notw1andnotw2 - value_four) ** 2) / value_four
    x2 = x2 + ((notw1andw2 - value_two) ** 2) / value_two
    #Print out the results
    print ("C(w1): ", w1)
    print ("C(w2): ", w2) 
    print ("C(w1w2): ", w1w2)
    print ("C(w1 && !w2)", w1andnotw2)
    print ("C(!w1 && w2)", notw1andw2)
    print ("C(!w1 && !w2)", notw1andnotw2)
    print ("Total Words: ", total_words)
    print ("")
    print ("0.05% Baseline: 3.841")
    print ("X^2:", x2)
    collocation = None
    degrees_of_freedom = 1
    if x2 <= 3.841:
        collocation = True
    else:
        collocation = False
    print ("Do we have a collocation?", collocation)

def main():
    #Example Test, will print that there is not a collocation
    chi_square ("the", "man", "brown")
    #Example Test, will print that there is a collocation
    chi_square ("Grand", "Jury", "brown")
