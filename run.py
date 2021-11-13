import random
import string
from words import words

def game_starts():
    """The initial stage of the game where a user's name is requested and if he/she would like to commence with the game.
    """
    print(
        """
        ██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██ 
        ██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██ 
        ███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██ 
        ██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██ 
        ██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████ 
                                                                                                                                                                                                       
        """
    )

    name = input('What is your name?\n')
    print(f'Hello, {name}')
    if input('Would you like to play the Hangman game? (Y)').upper() == "Y":
        hangman()

    else:
        print('Try Again')
        game_starts()

# function to get a random word from the list
def get_random_word():
    """
    A random word is picked from the list of words for the player to guess
    """
    word = random.choice(words)
    return word.upper()

def hangman():
    """Play the game"""
    word = get_random_word()
    word_letters = set(word) 
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # letters the user has guessed

    lives = 7