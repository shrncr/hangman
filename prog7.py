#SARA HRNCIAR
#ABI
#CSC 102 PROGRAM 7
# Modified hangman game. The only changes necessary were 1. assuring capitalized/uncapitalized
#letter guesses didn't make a difference, and 2. randomly choosing a new word from the text file
#in each run rather than keeping a static word like "computers"

import random

words = open(r'words.txt')
words = words.read()
wordList = words.split("\n")
word = random.choice(wordList).upper()
guessed_letters = []
guesses_left = 6
game_over = False

# create a function to display the current state of the game
def display_game_state():
    print("Word:", end=" ")
    for letter in word:
        if letter.upper() in guessed_letters: #modified it to make sure capitalization doesnt matter
            print(letter.upper(), end=" ")
        else:
            print("_", end=" ")
    print()
    print("Guesses left:", guesses_left)
    print()

# loop until the game is over
while not game_over:
    # display the current state of the game
    display_game_state()
    
    # ask the user for a guess
    guess = input("Guess a letter: ")
    
    # check if the guess is correct
    if guess.upper() in word: #assure capitalization doesnt matter
        guessed_letters.append(guess.upper())
        print("Correct!")
    else:
        guesses_left -= 1
        print("Incorrect.")
    
    # check if the game is over
    if guesses_left == 0:
        print("Game over! You ran out of guesses.")
        game_over = True
    elif set(guessed_letters) == set(word):
        print("Congratulations! You guessed the word.")
        game_over = True