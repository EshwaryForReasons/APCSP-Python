#########################################################
#                                                       #
#          DATA CLEANUP - BY ESHWARY MISHRA             #
#          LAST REVISED: 18/1/2022 (D/M/Y)              #
#                                                       #
#   People suck. Sometimes you need data, say from a    #
#   survey, and you get garbage. Completely useless     #
#   data. Bullsh*t. This program fixes that. By         #
#   inputting a list of data, this program will scan    #
#   through the list and clean up. Currently 0 is       #
#   considered invalid data. This program works by      #
#   going through the list both from the left and the   #
#   right and whenever it encounter a 0, it is replaced #    
#   by the right value.                                 #
#                                                       #
#########################################################

import random
import sys
from time import sleep

insults = [
    "Your a** is so hairy, it could single-handedly drive Gillette's out-of-stock.",
    "Even if you were gay, nobody would want to f*** you.",
    "I'M TOO LAZY TO PUT IN INSULTS"
]

premade_data = [213, 241, 43, 0, 234, 0, 12, 0, 432, 0, 55, 0, 6, 0, 2, 4, 0, 5, 0, 343534534534545345349857348579347857437957438574387598, 0]
user_data = []
final_list = []

def write(words):
    for char in words:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()

if input("Hey! Welcome to the data cleanup program. Here I clean your data! \nNow I am lazy, and if you are too, you can use a premade set of data, otherwise, you will need to enter your own. \nUse premade data? (y/n) ") == "n":
    write("Ok. Just know I have to code an entire input loop for your a**. \nHeres the deal. You enter the data you have. ONE BY ONE. \nPress enter after you enter the data. If you don't enter an integer I will insult you, so they better be integers. Got it? \nGood. \nOnce you have put in all the data type 'done' and we can move on.")

    while True:
        user_input = input("Enter data: ")

        if(user_input == "done"):
            write("Finally, Jesus!" if len(user_data) > 10 else "Great!")
            break
        elif user_input.isnumeric() == False:
            write(insults[random.randint(0, len(insults) - 1)])
        else:
            user_data.append(user_input)
else:
    user_data = premade_data

legit = len(user_data) - 1
left = 0
right = len(user_data) - 1

write("Original list: \n")
print(user_data)

while left < right:
    if user_data[left] != 0:
        left = left + 1
    else:
        legit = legit - 1
        user_data[left] = user_data[right]
        right = right - 1
if user_data[left] == 0:
    legit = legit - 1
    
for x in range(legit):
    final_list.append(user_data[x])

write("Final list: \n")
print(final_list)