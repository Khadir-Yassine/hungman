# Hangman Game

## Introduction
The "Hangman" game is a classic where the player must guess a hidden word by suggesting letters one at a time. If the suggested letter is in the word, it will be revealed. If not, a part of the hangman figure is drawn on the screen. The goal is to uncover the entire word before the hangman is fully drawn.

## Features
- *Random word selection*: A word is randomly chosen from a predefined list.
- *Interactive interface*: The current state of the word is dynamically updated after each guess.
- *Limited attempts*: The player has a limited number of incorrect guesses before the game is lost.

## How to Play
1. *Run the game*: Execute the hangman.py file.
2. *Start guessing*: Enter a letter to guess the word. If the letter is correct, it will appear in the word.
3. *Keep going*: Continue guessing until you either uncover the entire word or lose the game due to too many incorrect guesses.
4. *Win or lose*: The game ends when you correctly guess all the letters or the hangman figure is fully drawn.

## Requirements
- Python 3.x

## Installation
1. *Clone the repository*:
   bash
   git clone https://github.com/YourUsername/hangman-game.git
   
2. *Navigate to the project directory*:
   bash
   cd hangman-game
   
3. *Run the game*:
   bash
   python hangman.py
   

## Future Improvements
- *Difficulty levels*: Add options to choose difficulty levels (easy, medium, hard).
- *Hint system*: Provide hints to help players guess difficult words.
- *Add new words*: Allow players to add their own words to the word list.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- This game was inspired by the traditional "Hangman" game played with pen and paper.
