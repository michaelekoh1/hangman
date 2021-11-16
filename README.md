# HANGMAN GAME
[Hangman Game](https://hangman-game-2021.herokuapp.com/) - You can view the live game from here.

Hangman is a word guessing game which runs on the Code Institute mock terminal on Heroku. A player tries to guess a word by guessing letters within a certain number of guesses.

![The game viewed on different screen sizes](screenshots/responsiveindex.png)
*A screenshot of the start page of the game is viewed on different screen sizes, generated by [ami.responsivedesign.is](http://ami.responsivedesign.is/).

## User Experience

### User Stories
1. As a user, I would want to easily start the game.
2. As a user, I should be able to view my scores while am playing the game.
3. As a user, I should be able to exit the game on completion of the game. 
4. The game should be fun to play given the random words (easy and difficult) to guess.
        
## Features

- The user start with 7 lives and a score of 0
- For each valid letter, the user get 10 points
- For each wrong letter, the user losses 5 points
- If the user wins the match, the score is multiply by the amount of lives
    (example, the user won with 20 points and 2 lives, the total score is 40)

## Testing

The project was manually tested by the following ways:
- Tested in the local terminal and on the mock terminal on the deployed site of Heroku.
- Tested the python code through a PEP8 Linter using (http://pep8online.com/) and fixed the errors.

### Technologies Used

- Languages: Python.
- Random words generated: (https://randomwordgenerator.com/)


## Deployment

The site was deployed to GitHub pages using the Code Institute mock terminal on Heroku template.

- Steps for deployment
1. Fork or clone this repository
2. Create a new Heroku app
3. In "Settings" select "BuildPack" and select Python and Node.js..
4. Click on "Deploy" and select your deploy method and the repository.
5. Click "Connect" on selected repository.

## Credits
- Code Institute for the mock terminal to deploy the project.
- ASCII Art Generator - for creating the word art for game title.
- Youtube videos
- 

## Acknowledgement
I would like to take this opportunity to thank my mentor Jack Wachira for his great guidance in the accomplishment of this project and the whole learning experience.