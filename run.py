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

    # asking the user to choose an option
    option =  str(input('Choose a option: '))
    if option == "1":
        username = input('What is your name?: ')
        print(f"Hello, {username}. Welcome to The Game of Hangman!")
        hangman(username)
    elif option == "2":
        show_high_scores()

    game_starts()

def load_scores():
    """ Open the scores file and load the values, return a list with all the values
    inside the file, the list is returned empty if the file cant be found
    """
    score_list=[]
    if os.path.isfile(score_file):
        score_list = [line.rstrip('\n') for line in open(score_file)]

    return score_list

def show_high_scores():
    """ call function load_scores, and display it in the terminal
    """

    clear_terminal()
    scores_saved = load_scores()
    print('{:*^80}'.format(' HIGHSCORE TABLE ! '))
    print('\n' * 2)

    # itinerate over the scores loaded, and print each row with  score and username
    sorted_scores = sorted(scores_saved,reverse=True)

    for elem in sorted_scores:
        score = elem.split(";")[0]
        username = elem.split(";")[1]
        print('{:^80}'.format(f"{score}......{username.capitalize()}"))

    print('\n' * 2)
    # ask the user to press enter to go to main screen
    input("Press Enter to return to main screen  ")

def save_score(score, username):
    """ Load scores from higscore.txt file, add the current score of the user
    to the list of loaded values then, sort the list and only save the first 10 values
    """
    scores_saved = load_scores()

    scores_saved.append(f"{score};{username}")

    sorted_scores = sorted(scores_saved,reverse=True)

    with open(score_file, 'w+') as f:
        for x in range(len(sorted_scores)):
            f.write(f"{sorted_scores[x]}\n")
            if x >= 9:
                break


def clear_terminal():
    # clear all text in terminal, usefull for linux, macos and windows OS
    os.system('cls' if os.name == 'nt' else 'clear')