# Code by James Sprague
# January 14th, 2022
# Original game by Josh Wardle
# This is just a program I made for fun and to practice Python

# Printing text with color https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
# Printed list in different format https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
# Random https://www.geeksforgeeks.org/random-numbers-in-python/
# Text file into list https://www.kite.com/python/answers/how-to-read-a-text-file-into-a-list-in-python
# Changing all strings in a list https://www.kite.com/python/answers/how-to-replace-a-string-in-a-list-in-python
# List of 5 letter words https://eslforums.com/5-letter-words/#5_Letter_Words

class bcolors:
    CORRECT = '\033[92m'
    PRESENT = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

import random

word_file = open("wordle/5c_word_list.txt","r")
file_list = word_file.readlines()
word_list = []
for string in file_list:
    trimmed = string.upper().strip()
    word_list.append(trimmed)

play_again = 'Y'

while play_again == 'Y':
    print()
    ans = str(random.choice(word_list))
    correct = []
    present = []
    incorrect = []
    unconfirmed = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    finished = 0
    guesses = 0
    words_guessed = []
    attempts = 6
    colorful_guess = str('')
    while finished == 0:
        guess = str(input("Please enter your guess, must be a 5 letter word: ")).upper().strip()
        if len(guess) != 5:
            print(f'{bcolors.FAIL}Word must be 5 letters long, please try again!{bcolors.ENDC}')
        elif guess not in word_list:
            print(f'{bcolors.FAIL}Word is not in our list, please try again!{bcolors.ENDC}')
        else:
            print()
            colorful_guess = str('')
            for i in range(5):
                if guess[i] in unconfirmed:
                    unconfirmed.remove(guess[i])
                if guess[i] in ans:
                    if guess[i] == ans[i]:
                        colorful_guess = colorful_guess + (f'{bcolors.CORRECT}{guess[i]}{bcolors.ENDC} ')
                        if guess[i] not in correct:
                            correct.append(guess[i])
                        if guess[i] in present:
                                present.remove(guess[i])
                    else:
                        colorful_guess = colorful_guess + (f'{bcolors.PRESENT}{guess[i]}{bcolors.ENDC} ')
                        if guess[i] not in present:
                            if guess[i] not in correct:
                                present.append(guess[i])
                else:
                    colorful_guess = colorful_guess + (f'{bcolors.FAIL}{guess[i]}{bcolors.ENDC} ')
                    if guess[i] not in incorrect:
                            incorrect.append(guess[i])
            words_guessed.append(colorful_guess)
            print('\n'.join(words_guessed))
            print()
            incorrect.sort()
            present.sort()
            correct.sort()
            print(f'{bcolors.CORRECT}Correct:',end=' ')
            print(' '.join(correct))
            print(f'{bcolors.PRESENT}Present:',end=' ')
            print(' '.join(present))
            print(f'{bcolors.FAIL}Incorrect:',end=' ')
            print(' '.join(incorrect))
            print(f'{bcolors.ENDC}Unconfirmed:',end=' ')
            print(' '.join(unconfirmed))
            print()
            attempts = attempts - 1
            if guess == ans:
                print(f'Correct, the answer is {bcolors.CORRECT}{ans}{bcolors.ENDC}!')
                finished = 1
            elif attempts == 0:
                print(f'You used too many guesses, the correct answer was {ans}!')
                finished = 1
            else: 
                print(f'You have {attempts} guesses left!')

    play_again = str(input(f'Would you like to try again? ({bcolors.CORRECT}Y for Yes{bcolors.ENDC}, {bcolors.FAIL}N for No{bcolors.ENDC}): ')).upper().strip()

print('Thank you for playing!')