import random

insults = [
    "Your a** is so hairy, you could single-handedly drive Gillette's out-of-stock.",
    "Even if you were gay, nobody would want to f*** you.",
]

premade_data = [213, 241, 43, 0, 234, 0, 12, 0, 432, 0, 55, 0, 6, 0, 2, 4, 0, 5, 0, 343534534534545345349857348579347857437957438574387598, 0]
user_data = []

if input("Hey! Welcome to the data cleanup program. Here I clean your data! \nNow I am lazy, and if you are too, you can use a premade set of data, otherwise, you will need to enter your own. \nUse premade data? (y/n) ") == "n":
    print("Ok. Just know I have to code an entire input loop for your a**. \nHeres the deal. You enter the data you have. ONE BY ONE. Press enter after you enter the data. If you don't enter an integer I will insult you, so they better be integers. Got it? Good. \nOnce you have put in all the data type 'done' and we can move on.")

    while True:
        user_input = input("Enter data: ")

        if(user_input == "done"):
            break
        elif user_input.isnumeric() == False:
            print(insults[random.randint(0, len(insults) - 1)])
        else:
            user_data.append(user_input)
else:
    user_data = premade_data