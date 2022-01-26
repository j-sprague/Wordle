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
    keyboard = ['Q','W','E','R','T','Y','U','I','O','P','\n','A','S','D','F','G','H','J','K','L','\n  ','Z','X','C','V','B','N','M']
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
            print('---------------------------')
            dupe_check = []
            colorful_guess = str('')
            for i in range(5):
                if guess[i] in ans:
                    if guess[i] == ans[i]:
                        dupe_check.append(guess[i])
                        colorful_guess = colorful_guess + (f'{bcolors.CORRECT}{guess[i]}{bcolors.ENDC} ')
                        if guess[i] in keyboard:
                            keyboard[keyboard.index(guess[i])] = str(f'{bcolors.CORRECT}{guess[i]}{bcolors.ENDC}')
                        if str(f'{bcolors.PRESENT}{guess[i]}{bcolors.ENDC}') in keyboard:
                            keyboard[keyboard.index(str(f'{bcolors.PRESENT}{guess[i]}{bcolors.ENDC}'))] = str(f'{bcolors.CORRECT}{guess[i]}{bcolors.ENDC}')
                    else:
                        if guess[i] in dupe_check and ans.count(guess[i]) == dupe_check.count(guess[i]):
                            print(f'guess i in dupecheck WITH {i}')
                            colorful_guess = colorful_guess + (f'{bcolors.FAIL}{guess[i]}{bcolors.ENDC} ')
                        else:
                            dupe_check.append(guess[i])
                            colorful_guess = colorful_guess + (f'{bcolors.PRESENT}{guess[i]}{bcolors.ENDC} ')
                            if guess[i] in keyboard:
                                keyboard[keyboard.index(guess[i])] = str(f'{bcolors.PRESENT}{guess[i]}{bcolors.ENDC}')
                else:
                    colorful_guess = colorful_guess + (f'{bcolors.FAIL}{guess[i]}{bcolors.ENDC} ')
                    if guess[i] in keyboard:
                        keyboard[keyboard.index(guess[i])] = str(f'{bcolors.FAIL}{guess[i]}{bcolors.ENDC}')
            words_guessed.append(colorful_guess)
            print('\n'.join(words_guessed))
            print()
            print(' '.join(keyboard))
            print()
            attempts = attempts - 1
            if guess == ans:
                print(f'Correct, the answer is {bcolors.CORRECT}{ans}{bcolors.ENDC}!')
                finished = 1
            elif attempts == 0:
                print(f'You used too many guesses, the correct answer was {ans}!')
                finished = 1
            else:
                if attempts == 1:
                    print(f'You have one guess left!')
                else: 
                    print(f'You have {attempts} guesses left!')

    play_again = str(input(f'Would you like to try again? ({bcolors.CORRECT}Y for Yes{bcolors.ENDC}, {bcolors.FAIL}N for No{bcolors.ENDC}): ')).upper().strip()

print('Thank you for playing!')