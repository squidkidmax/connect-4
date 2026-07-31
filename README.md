# Connect Four

A graphical Connect Four game built with **Python**, **Pygame**, and **NumPy**. The game supports both local two-player matches and single-player matches against an AI opponent.

## Features

- Player vs. Player mode
- Player vs. AI mode
- Four AI difficulty levels
- Graphical interface built with Pygame
- Horizontal, vertical, and diagonal win detection
- Restart, difficulty-selection, and main-menu screens
- AI powered by the Minimax algorithm with alpha-beta pruning

## AI Difficulty

The AI difficulty is controlled by the Minimax search depth:

- Easy: depth 1
- Normal: depth 2
- Hard: depth 4
- Very Hard: depth 5

Higher difficulty levels search more possible moves and may take longer to respond.

## Technologies

- Python 3
- Pygame
- NumPy

## Project Structure

```text
connect-4/
├── connect_four.py
├── logo.png
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/squidkidmax/connect-4.git
cd connect-4
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

Alternatively:

```bash
pip install pygame numpy
```

## Running the Game

```bash
python connect_four.py
```

## Important Setup Note

The original source code uses an absolute path for the window icon:

```python
icon = pygame.image.load("/Users/maxnguyen/Downloads/logo.png")
```

For portability, place `logo.png` in the repository folder and change the line to:

```python
icon = pygame.image.load("logo.png")
```

You can also remove the icon-loading lines if no icon is required.

## How the AI Works

The AI evaluates possible moves using:

- Minimax search
- Alpha-beta pruning
- Center-column preference
- Horizontal, vertical, and diagonal scoring
- Defensive blocking against the player

The scoring function rewards positions containing two, three, or four connected pieces and penalizes positions where the opponent is close to winning.

## Controls

- Use the mouse to choose a column.
- Click to drop a piece.
- Use the menu buttons to select:
  - Player vs. Player
  - Player vs. AI
  - AI difficulty
  - Replay
  - Main menu
  - Quit

## Possible Improvements

- Add draw detection
- Prevent repeated button activation while holding the mouse button
- Separate the game logic, AI, and interface into different files
- Replace absolute file paths with relative paths
- Add sound effects and animations
- Add automated tests for win detection and AI decisions

## Author

Minh Khoi Nguyen
