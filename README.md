# Hangman Game

A command-line interface (CLI) Hangman game built with Python that features visual representations of the hangman as you play.

## Description

This classic Hangman game challenges players to guess a hidden word one letter at a time. Each incorrect guess brings the hangman closer to completion. The game currently uses fruit names as the word bank.

## Features

- Visual representation of the hangman that updates with each incorrect guess
- Word selection from predefined categories (currently using fruits)
- Input validation to ensure proper gameplay
- Option to play multiple games in one session

## How to Play

1. Run the game with `python main.py`
2. A random word will be selected and displayed as underscores
3. Guess one letter at a time
4. For each correct guess, the letter will appear in its correct position(s)
5. For each incorrect guess, part of the hangman will be drawn
6. Win by guessing all letters before the hangman is complete
7. Choose to play again after each game ends

## File Structure

- `main.py` - The main game logic
- `hangman_art.py` - Visual representations of the hangman at different stages
- `hangman_words.py` - Word lists categorized by theme (fruits, vegetables)

## Requirements

- Python 3.x

## Installation

1. Clone this repository

`git clone https://github.com/yourusername/hangman-game-python.git`

2. Navigate to the project directory

3. Run the game

`python main.py`

## Future Enhancements

- Add more word categories
- Implement difficulty levels
- Add scoring system
- Create a graphical user interface version

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for the details