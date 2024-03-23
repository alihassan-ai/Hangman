# AI2001 - Programming for AI
# Assignment 1: Hangman
# Name: Ali Hassan
# Roll Number: 22i-0541

# Driver Code
# -------------------------------------

# Imports
from src import Hangman
from src import get_word, load_words

# Constants
WORDLIST_FILENAME = "words.txt"
MAX_GUESSES = 6

# actually load the list of words and point to it with 
# the words_list variable so that it can be accessed
# from anywhere in the program
#ok

words_list = load_words()

# Welcome message
print("Welcome to Hangman!")

while True:
    
    # Game start messages
    print("\nNew Game!")
    print("Try to guess the word.")
    print("You have", MAX_GUESSES, "incorrect guesses allowed.")

    secret_word = get_word(words_list)
    hangman = Hangman(secret_word, MAX_GUESSES)
    hangman.play()

    # Print overall statistics
    print("\nOverall Statistics:")
    print("Total Games Played:", Hangman.total_games)
    print("Total Wins:", Hangman.wins)
    print("Total Losses:", Hangman.total_games - Hangman.wins)
    