#Name:          Samantha Garcia
#Section:       27F3
#Assignment:    06
#Due Date:      February 21st, 2018

import re
import os
import nltk
from os.path import isfile, join

#Return a list of words found in the Santa Barbara Corpus
def get_corpus_list ():
    path = os.path.dirname(os.path.realpath(__file__)) + "\\sbcorpus"
    files = [f for f in os.listdir(path) if os.path.isfile(join(path, f))]
    corpus = []
    for i in range (len (files)): 
        temp_file = open (path + "\\" + files[i], 'r')
        temp_contents = re.findall(r'I|A|[^0-9|(0-9).|0-9 |(A-Z:)|\s]*', temp_file.read())
        for w in temp_contents:
            if w.isalpha():
                corpus.append(w)
    return corpus

#Return the probability of a bigram in the Conditional Frequency Distribution
def get_probability (prev_word, curr_word, cfd):
    dictionary = {'a' : 'abc', 'b' : 'abc', 'c' : 'abc', 'd' : 'def', 'e' : 'def', 'f' : 'def', 'g' : 'ghi', 'h' : 'ghi', 'i' : 'ghi', 'j' : 'jkl', 'k' : 'jkl', 'l' : 'jkl','m' : 'mno', 'n' : 'mno', 'o' : 'mno', 'p' : 'pqrs', 'q' : 'pqrs', 'r' : 'pqrs', 's' : 'pqrs', 't' : 'tuv', 'u' : 'tuv', 'v' : 'tuv', 'w' : 'wxyz', 'x' : 'wxyz', 'y' : 'wxyz', 'z' : 'wxyz'}
    #Form the appropriate regular expression
    regex_exp = '^'
    for char in curr_word:
        regex_exp = regex_exp + '[' + dictionary[char] + ']'
    regex_exp = regex_exp + '$'
    regex_word = re.compile(regex_exp)
    for i in range (len (cfd[prev_word])):
        temp_word = cfd[prev_word].most_common(len (cfd[prev_word]))[i][0]
        #Search if the word is common using regular expressions
        if (re.search(regex_word, temp_word)):
            return temp_word
    return curr_word

#Implementation of HW6, takes in a text message typed in a T9 system and returns an approximation to what it might have meant
def problem_1 (text_message):
    #Get the corpus list
    corp_list = get_corpus_list()
    corp_list = [w.lower() for w in corp_list]
    #Create a bigram list and conditional frequency distribution
    bigrams_list = list(nltk.bigrams (corp_list))
    cfd = nltk.ConditionalFreqDist(bigrams_list)
    text_message = re.findall(r'[0-9a-zA-Z ]+', text_message)
    text_message = ' '.join(text_message)
    text_message = text_message.split(" ")
    text_message = [w.lower() for w in text_message]
    final_msg = []
    prev_word = text_message[0]
    #For each word in the message, get the probability that it follows the previous word; if not, change it using the t9 regular expressions
    for entry in text_message:
        entry = entry
        if entry == 'i':
            new_word = 'i'
        elif entry == 'a':
            new_word = 'a'
        else:
            new_word =(get_probability(prev_word, entry, cfd))
        final_msg.append (new_word)
        prev_word = new_word
    return ' '.join(final_msg)
            
#Declare the main function        
def main ():
    txt_msg = "I an really out me it. I lost ox bbq. Can wot bone un het of?"
    print ("Text Message Without Translation: ", txt_msg)
    print ("Translated Result: ", problem_1(txt_msg))

#Call the main Function
main()

