#Name:          Samantha Garcia
#Section:       27F3
#Assignment:    10
#Due Date:      April 13th, 2018

import nltk
import collections
import random
from nltk.corpus import brown
from collections import defaultdict
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet as wn

###Number 1###
def problem_1 ():
    ##Part A##
    print ("####QUESTION 1####")
    tagged_text = nltk.corpus.brown.tagged_words()
    counts = defaultdict(int)
    nouns = [w for (w, t) in tagged_text if t.startswith('N')]
    for w in nouns:
        counts[w.lower()] += 1
    print ('##Part A##')
    for w in counts:
        if (w + 's') in counts:
            if counts [w + 's'] > counts [w]:
                print (w)
    ##Part B##
    print ('##Part B##')
    word_dict = nltk.defaultdict(set)
    for word,tag in tagged_text:
        word_dict[word.lower()].add(tag)
    lengths = (len(word_dict[word]) for word in word_dict)
    maximum = max (lengths)
    for word, tag in word_dict.items():
        if len (tag) == maximum:
             print ("Word: ", word, " Tag: ", tag)
             break
    ##Part C##
    print ('##Part C##')
    cfd = None
    cfd = nltk.FreqDist(tag for (word, tag) in tagged_text)
    print (cfd.most_common(20))
    ##Part D##
    print ("##Part D##")
    tagged_text_universal = nltk.corpus.brown.tagged_words(tagset='universal')
    bigrams = nltk.bigrams (t for w, t in tagged_text_universal)
    dist = nltk.FreqDist (first for first, second in bigrams if second == 'NOUN')
    print (dist.most_common (12))
    print ("DET: Determiner, ADJ: Adjective, NOUN: Noun, ADP: Adposition, .: Punctuation Marks, VERB: Verb, CONJ: Conjunction, NUM: Numeral, ADV: Adverb, PRT: Particle, PRON: Pronoun, X: Other ")

def problem_2 ():
    documents = [(list(movie_reviews.words(fileid)), category)
                 for category in movie_reviews.categories()
                 for fileid in movie_reviews.fileids(category)]  
    random.shuffle (documents)
    all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
    word_features = list (all_words)[:2000]
    featuresets = [(document_features(d, word_features), c) for (d, c) in documents]
    train_set, test_set = featuresets[100:], featuresets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print ("####QUESTION 2####")
    print("Accuracy: ", nltk.classify.accuracy(classifier, test_set))
    print ("Accuracy is lower because a word is used in a particular context, synsets have no correlation to what is being reviewed. ")
    
def document_features (document, word_features):
    document_words = set (document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
        for temp in wn.synsets(word):
            features['synsets({})'.format(word)] = temp
        return features

def main ():
    problem_1 ()
    problem_2 ()

main ()
