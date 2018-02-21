#Name:          Samantha Garcia
#Section:       27F3
#Assignment:    03
#Due Date:      January 31st, 2018

import nltk

#Number 1 (2.4) in HW3

print ('################ Number 1 ################')

#Generating list for each of the words through time
from nltk.corpus import state_union as su
total = []
men = []
women = []
people = []
for s in su.fileids():
	length_women = 0
	length_men = 0
	length_people = 0
	length = 0;
	for w in su.words (s):
		if w.lower() == 'women':
			length_women += 1
			length += 1
		elif w.lower() == 'men':
			length_men += 1
			length += 1
		elif w.lower() == 'people':
			length_people += 1
			length += 1
	total.append (length)
	women.append (length_women)
	men.append (length_men)
	people.append (length_people)
	length_women = 0
	length_men = 0
	length_people = 0
	length = 0;
print ('Total usage of words: ', total, '\n')
print ('Usage of the word men: ', men, '\n')
print ('Usage of the word women: ', women, '\n')
print ('Usage of the word people: ', people, '\n')

#Extra: Producing a dispersion plot to see the usages of the words over time

cfd = nltk.ConditionalFreqDist (
		(genre, word)
		for genre in su.fileids()
		for word in su.words(genre)
		if word.lower() == 'women' or word.lower() == 'men' or word.lower() == 'people')

from nltk.draw.dispersion import dispersion_plot
words_watch = ['men', 'women', 'people']
dispersion_plot (su.words (), words_watch, ignore_case = True)

#Number 2 (2.13) in HW3

print ('################ Number 2 ################')

from nltk.corpus import wordnet as wn
nnw = wn.all_synsets('n')
nouns = list (nnw)
print ('Length of synsets', len(nouns))
yes = []
for w in nouns:
	if len (w.hyponyms()) != 0:
		yes.append (w)
print ('Length of synsets with hyponyms', len(yes))
print ('Percentage of noun synsets with no hypnoyms' ,(100 - (len (yes) / len (nouns)) * 100))

#Number 3 (2.19) in HW3

print ('################ Number 3 ################')
#Creating a Confitional Frequency Distribution to tabulate all of the words in each genre included in the corpus
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist (
	(genre, word)
	for genre in brown.categories()
	for word in brown.words (categories=genre))
genres = brown.categories()
modals = ['mysterious', 'sad', 'kiss', 'death', 'congress', 'beautiful', 'cry', 'leave', 'love', 'pope', 'horrible']
cfd.tabulate (conditions=genres, samples=modals)

#Number 4 in HW3

print ('################ Number 4 ################')

def censor (bad, good, text) :
    #Split the text up into a list
    text_list = text.split (" ")
    #Go through each element in the list and replace the text
    for word in text_list:
        for bad_word in bad:
            if word == bad_word:
                index_bad_word = bad.index(bad_word)
                good_word = good [index_bad_word]
                text_list[text_list.index(word)] = good_word
    new_text = " ".join(text_list)
    return new_text


bad_words = [ 'hell', 'Queequeg', 'dumpling' ]
better_words = [ 'heck', 'Tony', 'core' ]
sample_text = 'In one word , Queequeg , said I , rather digressively ; hell is an idea first born on an undigested apple - dumpling'
print( censor( bad_words, better_words, sample_text ) )

    
