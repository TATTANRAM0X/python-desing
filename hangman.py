
# from operator import attrgetter
# from symbol import import_as_name


list1 = ['elefantin', 'mirrincha', 'medellin', 'negra', 'kevin', 'mona', 'bella', 'jhonatan', 'ligia', 'teresa', 'carlos']
import random
from r import hangman
randompos = random.randint(0, len(list1) - 1)
chosenword = list1[randompos]
dashword = len(chosenword) * '_'
print("{}".format(dashword))
i = 0
attempts = 8

while i < attempts:
    letter = input("enter a letter: ")
    flag = 0
    for j in range(len(chosenword)):
        if letter == chosenword[j]:
            dashword = dashword[:j] + letter + dashword[j+1:]
            flag = 1

    if flag == 0:
        i += 1
        print("letter not found")
        print("You have {} of {} attempts".format(attempts - i, attempts))
        hangman(i)
    print(dashword)
    if dashword == chosenword:
        print("CONGRATULATIONS, YOU WIN !!!")
        break
if dashword != chosenword:
    print(f"The word is {chosenword}")
    print("YOU LOSE, KEEP TRYING")
