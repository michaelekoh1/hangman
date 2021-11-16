import random
import string
from word_list import words
from hangman_stages import stages
import os   # used to check if file with scores exists

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
    option = str(input('Choose an option from the menu: '))
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
    score_list = []
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

    # itinerate over the scores loaded, print each row with  score and username
    sorted_scores = sorted(scores_saved, reverse=True)

    for elem in sorted_scores:
        score = elem.split(";")[0]
        username = elem.split(";")[1]
        print('{:^80}'.format(f"{score}......{username.capitalize()}"))

    print('\n' * 2)
    # ask the user to press enter to go to main screen
    input("Press Enter to return to main screen  ")


def save_score(score, username):
    """ Load scores from highscore.txt file, add the current score of the user
    """
    scores_saved = load_scores()

    scores_saved.append(f"{score};{username}")

    sorted_scores = sorted(scores_saved, reverse=True)

    with open(score_file, 'w+') as f:
        for x in range(len(sorted_scores)):
            f.write(f"{sorted_scores[x]}\n")
            if x >= 9:
                break


def clear_terminal():
    # clear all text in terminal, usefull for linux, macos and windows OS
    os.system('cls' if os.name == 'nt' else 'clear')


# function to get a random word from the list of words
def get_random_word():
    """
    A random word is picked from the list of words for the player to guess.
    The words are listed in the file words.py
    """
    word = random.choice(words)
    return word.upper()


def hangman(username):
    """Playing the Game, all letters are processed in a uppercase mode
    """
    word = get_random_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # letters the user has guessed

    lives = 7
    score = 0
    while len(word_letters) > 0 and lives > 0:
        clear_terminal()
        print (f"User Name: {username.capitalize()}         Score: {score}")
        print('You have', lives, 'lives remaining')
        print('Letters used: ', ' '.join(used_letters))

        # Current word is (ie W O - D)
        word_list = [
            letter if letter in used_letters else '_' for letter in word]
        print(stages[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess the letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                score += 10
                word_letters.remove(user_letter)

            else:
                score -= 5
                lives = lives - 1  # A life is lost when wrong
                print('This letter is not in this word.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character! Kindly try again.')

    if lives == 0:
        print(stages[lives])
        print('Your Dead! Sorry. The word was', word)
    else:
        print('You have guessed the right word', word, '\nCongratulations!!!')

    if lives > 0:
        score *= lives
    print (f"You score is: {score}")
    # if score is bigger than 0, then try to save the score
    if score > 0:
        save_score(score, username)
    restart_game(username)


def restart_game(username):
    """Player has an option to restart the game"""
    game_restart = False

    while not game_restart:
        restart = input('Would you like to play again? (Y/N): ').upper()

        if restart == "Y":
            game_restart = True
            hangman(username)

        elif restart == "N":
            game_restart = True
            print('Goodbye! See you soon')
            game_starts()

        else:
            print('Select Y or N. Please try again.')


if __name__ == "__main__":
    game_starts()
