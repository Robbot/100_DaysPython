#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
# word = []
# for letter in chosen_word:
#     word.append("_")
# print(word)
display = []
word_lenght = len(chosen_word)
for _ in range(word_lenght):
    display += "_"
print(display)
guess = input("Guess a letter: ").lower()

#Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
#It was mine piece of code - it does work too, but maybe hers is better.
# i = 0
# display = []
# for letter in chosen_word:
#     if letter == guess:
#         display.insert(i,letter)
#     else:
#         display.insert(i,"_")
#     i += 1
for position in range(word_lenght):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

#Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)