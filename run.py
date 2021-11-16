import random
import string
from word_list import words
from hangman_stages import stages
import os # used to check if file with scores exists

# name of the file where higHscores will be stored
score_file = "highscores.txt"

def game_starts():
    """The initial stage of the game where a user's name is requested and if
    he/she would like to commence with the game.
    Also show a new menu with highscores table
    """

    clear_terminal()
    print ("""
\t  ██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██
\t  ██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██
\t  ███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██
\t  ██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██
\t  ██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████
    """)
    print('{:*^80}'.format(' WELCOME TO HANGMAN ! '))
    print('\n' * 4)
    print('{:^80}'.format(' 1: PLAY GAME '))
    print('{:^80}'.format(' 2: HIGH SCORES '))
    print('{:^80}'.format(' 3: QUIT '))
    print('\n' * 4)