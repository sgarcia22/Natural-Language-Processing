#Name:          Samantha Garcia
#Section:       27F3
#Assignment:    086
#Due Date:      March 23rd, 2018

import nltk, re
from nltk.corpus import brown, treebank
class POS_Tag_Data:
    # given a corpus,
    # place the tuples of word/tag pairs into tagged
    # make the words in tagged / words lists lower case 
    # use the punctuation selection provided
    def __init__( self, corpus, punctuation=False, universal=True ) :
        if universal:
            temp = corpus.tagged_words(tagset='universal')
        else:
            temp = corpus.tagged_words()
        tagged = []
        if punctuation:
            tagged = temp
        else:
            #Remove all punctuation
            for w, t in temp:
                if t != '.':
                    no_punct = [w, t]
                    tagged.append(no_punct)
        tags = [tag for (word, tag) in tagged]
        words = [w.lower() for w in corpus.words()]
        #Assign the lists to the self object
        self.tagged = tagged
        self.tags = tags
        self.words = words
        
    # find all index positions of the tag provided
    def all_tag_inds( self, tag ) :
        inds = []
        for i in range(0, len(self.tags)):
            if self.tags[i] == tag:
                inds.append(i)
        return inds

    # find all index positions of the word provided
    def all_word_inds( self, word ) :
        inds = []
        for i in range(0, len(self.words)):
            if self.words[i] == word:
                inds.append(i)
        return inds

#Test Cases
def main():
    # sample test cases to consider
    ptd_brown = POS_Tag_Data( brown )
    noun_inds = ptd_brown.all_tag_inds( 'NOUN' )
    work_inds = ptd_brown.all_word_inds( 'work' )
    ptd_treebank = POS_Tag_Data( treebank, universal=False )
    nnp_inds = ptd_treebank.all_tag_inds( 'NNP' )
    work_inds = ptd_treebank.all_word_inds( 'work' )
    #Print out some of the results
    print (noun_inds[:50])
    print (nnp_inds[:50])
    print (work_inds[:50])
