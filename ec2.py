#Name:          Samantha Garcia
#Section:       27F3
#Assignment:    EC2
#Due Date:      April 5th, 2018

import nltk
import re
import os
import random

def iRobot ():
    #Get a random question from the ones given by the judges
    #Get all of the files    
    set_questions = []
    set_human_answers = []
    set_robot_answers = []
    all_files = []
    for folder in os.listdir("Loebner-logs-2003"):
        for file in os.listdir(os.path.join("Loebner-logs-2003\\", folder)):
            if file.endswith(".log"):
                temp_file = open ("Loebner-logs-2003\\" + folder + "\\" + file)
                count = 0
                #Get the line where the questions start
                for i, line in enumerate (temp_file):
                    if re.match(r"[0-9]{4}", line):
                        if (re.search(r"PROGRAM", line) != None):
                            set_robot_answers.append (line)
                        elif (re.search(r"JUDGE", line) != None):
                            set_questions.append (line)
                        else:
                            set_human_answers.append (line)                   
    #Remove extra characters the string does not need with regex
    questions = []
    human_answers = []
    robot_answers = []
    for i in set_questions:
        temp = re.sub(r'([0-9]*-|[0-9]*)* ([A-Z]*: )|(\?|\.)', '', i)
        questions.append (temp.lower())
    for i in set_human_answers:
        temp = re.sub(r'([0-9]*-|[0-9]*)* ([A-Z]*: )|(\?|\.)', '', i)
        human_answers.append (temp.lower())
    for i in set_robot_answers:
        temp = re.sub(r'([0-9]*-|[0-9]*)* ([A-Z]*: )|(\?|\.)', '', i)
        robot_answers.append (temp.lower())
    #Split up the words
    all_robot_words = []
    all_human_words = []
    for i in robot_answers:
        temp = i.split(" ")
        temp_list = []
        for j in temp:
            temp_two = re.sub(r'(\?|\.|(\\n)|\n)', '', j)
            temp_list.append (temp_two)            
        all_robot_words.extend (temp_list)
    for i in human_answers:
        temp = i.split(" ")
        temp_list = []
        for j in temp:
            temp_two = re.sub(r'(\?|\.|(\\n)|\n|\!)', '', j)
            temp_list.append (temp_two)            
        all_human_words.extend (temp_list)
    #Get a random question from the list and get the response
    choice = (input (random.choice(questions))).lower()
    #Determine if the response is from a PROGRAM or not
    labeled_sets = ([(program, 'Computer') for program in robot_answers] + [(none_program, 'Human') for none_program in human_answers])
    random.shuffle(labeled_sets)
    feature_sets = [(computer_features(n, all_robot_words, all_human_words), computer) for (n, computer) in labeled_sets]
    train_set, test_set = feature_sets[100:], feature_sets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    final_answer = choice.split(" ")
    output = classifier.classify(computer_features(final_answer, all_robot_words, all_human_words))
    print (output)

def computer_features (input_string, robot, human):
    freq_dist_robot = nltk.FreqDist (robot)
    freq_dist_human = nltk.FreqDist (human)
    count_robot = 0
    count_human = 0
    for i in input_string:
        count_robot = count_robot + freq_dist_robot [i]
        count_human = count_human + freq_dist_human [i]
    count_robot = count_robot / len (input_string)
    count_human = count_human / len(input_string)
    return {'robot': count_robot, 'human': count_human}

def main():
    iRobot()

main()
