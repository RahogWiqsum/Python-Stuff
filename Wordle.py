# TO DO LIST:
# - Figure out how to check if the word is accurate
# - Figure out how to format each thing
# - How to check for letter locations

import random
List = ["Plate", "World", "Silly" ]
WordIndex = random.randrange(len(List))
Word = List[WordIndex]
Guesses = 6

# Variables that keep track of each letter in the word
Letter_1 = Word[0]
Letter_2 = Word[1]
Letter_3 = Word[2]
Letter_4 = Word[3]
Letter_5 = Word[4]

# Variables to check if the letter in a certain slot has been solved
Letter_1_Solved = False
Letter_2_Solved = False
Letter_3_Solved = False
Letter_4_Solved = False
Letter_5_Solved = False
# FUNCTIONS

def NewAttempt():
    print("NEW ATTEMPT:")
    print("\n \n \n \n")
    print(Word)

NewAttempt()