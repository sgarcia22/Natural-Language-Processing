#Name:          Samantha Garcia
#Section:       27F3
#Assignment:    05
#Due Date:      February 16th, 2018

import nltk
import re

#Number One
#Part a
def number_one_a (word):
    beginning = re.match(r'^[^aeiou]*', word);
    new_word = word[len(beginning.group(0)):]
    new_word = new_word + beginning.group(0) + "ay"
    return new_word
#Part b
def number_one_b (string):
    new_text = string.split(" ")
    latin = []
    for word in new_text:
        latin.append (number_one_a (word))
    return " ".join(latin)
#Number Two
def number_two (string):
    if (re.match(r'^([0-9]{1,5}) (N|NW|NE|SW|SE|)(S|W|E|n|nw|ne|sw|se|s|w|e)? ([0-9]{1,3})(ST|ND|RD|TH|st|nd|rd|th)? (RD|AVE|DR|TERR|ST|CIR|rd|ave|dr|terr|st|cir)(, Gainesville, FL 326)([0-9]{2})',string)):
        return "The address is valid."
    else:
        return "The address is not valid."
#Main Function
def main ():
    #Will print the pig latin version of the string
    hello = "the fat brown dog jumped over the lazy fox"
    print (number_one_b (hello))

    address = "55755 se 33RD CIR, Gainesville, FL 32699"
    #Will print valid
    print (number_two(address))

    address = "55755 se 33RD CIRD, Gainesville, FL 32699"
    #Will print not valid
    print (number_two(address))

    address = "3461 sw 2nd ave, Gainesville, FL 32605"
    #Will print valid
    print (number_two(address))

main()
