# Wordle

Version of Wordle that can be played entirely within the command-line. This was a side-project created in early 2022 to familiarize myself with Python.

## wordle.py

Version of Wordle entirely playable within the command-line. Differently colored text may not show properly on Git; tested with PowerShell. Player can choose between 4, 5, or 6 letter words. All the words are ripped from their respective text file located in the repository. ("4c_word_list.txt")

![image](https://user-images.githubusercontent.com/73149971/230830421-2185367d-2514-4f8e-a456-13c94d991411.png)

## fun_killer.py

Searches for the answer to a Wordle puzzle based on information you already know: the letters that aren't in the word, the letters that are in the word with an unknown position, and letters that are in the word at a confirmed position. Will print back an array of words that match the parameters given by the user based on the words in "5c_word_list.txt". Guesses only work for 5 letter words, but this could be easil repurposed for the 4 letter and 6 letter words if desired.

Example: fun_killer.py (picture 1) trying to guess the answer for wordle.py (picture 2).
![image](https://user-images.githubusercontent.com/73149971/230830859-55fbf7be-2cfd-48b4-8f1b-53d192543ac6.png)

![image](https://user-images.githubusercontent.com/73149971/230830902-15e3cfe0-9148-4096-bee0-178fa268cdaf.png)
