# Sys module is used to access command line arguments for console
# Random module to ask question randomly

import sys
import random
if len(sys.argv) < 2:
    print("Please supply a the file name")
    exit(1)

# Open file in read mode and pass 2nd arg as file parameter
file_name = sys.argv[1]
open_file = open(file_name, 'r')

# Create dictionary of key-value pair for states and their capitals

question_dict = {}
for line in open_file:
    entry = line.strip().split(',')
    question = entry[0]
    answer = entry[1]
    question_dict[question] = answer

open_file.close()

print("Welcome to the State Capital quizz... ")
print("Type 'quit' to stop the quiz at anytime \n")


questions = list(question_dict.keys())
counter_right, counter_wrong = 0, 0
while True:
    question = random.choice(questions)
    answer = question_dict[question]

    print("Question : ", question)
    user_input = input("Your guess --> \t").capitalize().strip()
    if user_input == 'Quit':
        print("Your score ", counter_right, 'out of', counter_right+counter_wrong)
        print("Thanks for playing!  We will meet again! ")
        break
    elif user_input == answer:
        print("Correct")
        counter_right = counter_right + 1
    else:

        print("Sorry! Answer was ", answer)
        counter_wrong = counter_wrong + 1

print(counter_wrong, counter_right)
