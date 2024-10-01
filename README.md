# Cup Ordering Game

Welcome to the **Cup Ordering Game**, a fun and interactive game inspired by the viral cup matching game. Players aim to arrange a set of numbers in a specific order by swapping their positions. The game features a simple graphical interface and tracks your attempts to help you beat your high score!

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Gameplay](#gameplay)
- [High Score Tracking](#high-score-tracking)

## Features

- **Intuitive Interface**: Easy-to-use graphical interface with number buttons.
- **Randomized Gameplay**: Each game starts with a different secret order of numbers.
- **Feedback System**: Get real-time feedback on how many numbers are correctly placed.
- **High Score Tracking**: Keep track of your best attempts and compete against yourself!

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- Pillow library for image handling

To install Pillow, you can use pip:

```bash
pip install Pillow
```

## Installation

1. Clone this repository or download the ZIP file
2. Navigate to the project directory
3. Ensure you have the necessary images (`1.png`, `2.png`, `3.png`, `4.png`, `5.png`) in the project directory.

## Usage

To run the game, execute the following command:

```bash
python cup_UI.py.py
```
## Gameplay

1. **Objective**: The goal is to rearrange the numbers (1 to 5) to match a hidden secret order by swapping their positions.
2. **Swapping Numbers**: Click on two numbers to swap their positions.
3. **Check Your Guess**: Press the "Check Order" button to see how many numbers are correctly placed. Your attempt counter will increment with each guess.
4. **Reset Game**: Use the "Reset Game" button to start over anytime.

## High Score Tracking

- The game keeps track of your high score based on the fewest attempts taken to correctly guess the order. 
- High scores are saved in a file named `highscore.txt`, which will be created automatically in the project directory if it doesn’t exist.

## License

This project is licensed under the MIT License. Feel free to modify and distribute it as you like!
