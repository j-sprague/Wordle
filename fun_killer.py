class bcolors:
    CORRECT = '\033[92m'
    PRESENT = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

next_hint = 'b'
confirmed = ['_','_','_','_','_']
unknown_location = []
not_present = []
possible_ans = []

while next_hint.strip().upper() != 'N':
    character = input(f'What letter do you know the position of? (if none reply No): ').strip().upper()
    if character.isalpha() and len(character) == 1:
        while True:
            spot = input(f'What position is the letter in? (1-5): ')
            if not spot.isdigit() or int(spot) > 5 or int(spot) < 1:
                print("Please enter a number from 1-5")
            else:
                confirmed[int(spot)-1] = character
                print(f'Currently confirmed: ' + ' '.join(confirmed) + "\n")
                break
    elif character == 'NO':
        next_hint = 'N'
    else:
        print("Please enter a confirmed letter or the word 'No' if you do not have one.\n")

next_hint = 'y'

while next_hint.strip().upper() != 'N':
    character = input(f'What letter do you not know the position of? (if none reply No): ').strip().upper()
    if character.isalpha() and len(character) == 1:
        while True:
            spot = input(f'What position is the letter NOT located at? (1-5): ')
            if not spot.isdigit() or int(spot) > 5 or int(spot) < 1:
                print("Please enter a number from 1-5")
            else:
                unknown_location.append([character,spot])
                break
    elif character == 'NO':
        next_hint = 'N'
    else:
        print("Please enter an unconfirmed letter or the word 'No' if you do not have one.\n")
    

next_hint = 'y'

while next_hint.strip().upper() != 'N':
    character = input(f'What letter do you know is NOT in the word? (if none reply No): ').strip().upper()
    if character.isalpha() and len(character) == 1:
        not_present.append(character)
    elif character == 'NO':
        next_hint = 'N'
    else:
        print("Please enter a not present letter or the word 'No' if you do not have one.\n")

print(f'Currently confirmed: ' + ' '.join(confirmed))
print(f'Unknown location: ',end=' ')
for i in unknown_location:
    print(' located at '.join(i),end='')
    if not unknown_location.index(i) == len(unknown_location) - 1:
        print(', ',end='')
print('\nNot in word: ' + ', '.join(not_present))

word_file = open('5c_word_list.txt',"r")
file_list = word_file.readlines()
word_list = []

for string in file_list:
    trimmed = string.upper().strip()
    word_list.append(trimmed)

#print(word_list)

for word in word_list:
#    word = 'REACT'
#    print("Entering for loop word in word list")
    try:
#        print("In try block with " + word)
        for let in not_present:
            if let in word:
#                print("Going to raise exception! at NOR PRESENT")
                raise Exception
#        print("1")
        for let in unknown_location:
#            print(f'if {let[0]} not in {word}')
            if let[0] not in word:
#                print("Going to raise exception! at UNKNOWN LOCATION 1")
                raise Exception
#            print(f'if {let[0]} == {word[int(let[1])-1]}')
            if let[0] == word[int(let[1])-1]:
#                print("Going to raise exception! at UNKNOWN LOCATION 2")
                raise Exception
#        print("2")
        for let in range(5):
            if confirmed[let] != '_' and confirmed[let] != word[let]:
#                print("Going to raise exception! at CONFIRMED")
                raise Exception
#        print("3")
        possible_ans.append(word)
    except Exception:
        print('',end='')

print(possible_ans)