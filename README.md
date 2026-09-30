# 2048 Game

## Overview

2048 Game is a Python-based command-line implementation of the classic 2048 puzzle game.

The game is played on a 4 × 4 grid. The player moves numbered tiles using the W, A, S and D keys. When two tiles with the same value collide, they are merged into one tile with double the value.

The project is developed using a modular Python structure so that board creation, tile generation, movement, game-state checking, scoring, display and testing are handled separately.

## Features

- 4 × 4 game board
- Random generation of 2 and 4 tiles
- Move tiles Up, Down, Left and Right
- Merge matching tiles
- Automatic score calculation during moves
- Highest tile display
- Win condition when the 2048 tile is created
- Game-over condition when no valid moves remain
- Restart game using R
- Quit game using Q
- Invalid command handling
- Separate modules for different game functions
- Movement testing using a separate test file

## Controls

| Key | Action |
|-----|--------|
| W / w | Move Up |
| S / s | Move Down |
| A / a | Move Left |
| D / d | Move Right |
| R / r | Restart Game |
| Q / q | Quit Game |

## Technologies Used

- Python 3
- Python standard library
- Random module
- Git and GitHub
- Command-line interface

## Project Structure

```text
2048-Game/
│
├── main.py
│
└── game2048/
    ├── __init__.py
    ├── board.py
    ├── display.py
    ├── game_state.py
    ├── movement.py
    ├── score.py
    ├── tiles.py
    └── test_movement.py
```

### Module Description

- `main.py` - Controls the main game loop and connects the different modules.
- `board.py` - Creates and initializes a new 4 × 4 game board.
- `display.py` - Displays instructions, the game board and the highest tile.
- `game_state.py` - Checks whether the player has won, lost or can continue.
- `movement.py` - Implements tile compression, merging and movement in all four directions.
- `score.py` - Contains score calculation functionality.
- `tiles.py` - Generates new tiles and places 2 or 4 in an empty position.
- `test_movement.py` - Tests the movement functionality.

## How the Game Works

1. The game creates an empty 4 × 4 board.
2. A starting tile is randomly added to the board.
3. The available commands are displayed.
4. The player enters a movement command.
5. The selected movement is processed.
6. Matching tiles are merged.
7. A new tile is added when the board changes.
8. The score and highest tile are displayed.
9. The game checks whether the player has won or lost.
10. The process continues until the player wins, loses or quits.

## Installation

### Requirements

Python 3 must be installed on the computer.

No external Python packages are required for the current implementation.

### Steps

1. Clone or download this repository.
2. Open the project folder in a terminal.
3. Make sure the `game2048` folder is in the same project directory as `main.py`.
4. Run the game using:

```bash
python main.py
```

## Testing

The project includes a movement test file.

Run:

```bash
python test_movement.py
```

The test checks the `move_left()` functionality using a sample board and displays whether the board changed, the score gained and the resulting board.

## Input and Output

### Input

The player enters one of the following commands:

- W / w
- A / a
- S / s
- D / d
- R / r
- Q / q

### Output

The program displays:

- Current 4 × 4 board
- Current score
- Highest tile
- Game status
- Win or game-over message
- Error message for invalid commands

## System Architecture

```text
                    ┌─────────────┐
                    │   main.py   │
                    │ Main Game   │
                    │    Loop     │
                    └──────┬──────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
    ┌───────────┐    ┌────────────┐   ┌──────────────┐
    │  board.py │    │ display.py │   │ game_state.py│
    │ Board     │    │ User       │   │ Win/Loss     │
    │ Creation  │    │ Interface  │   │ Checking     │
    └───────────┘    └────────────┘   └──────────────┘
          │
          ▼
    ┌──────────────┐
    │ movement.py  │
    │ Move/Merge   │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │   tiles.py   │
    │ New Tiles    │
    └──────────────┘

    score.py
    Score calculation utility

    test_movement.py
    Movement testing
```

## Non-Functional Considerations

### Usability
The game uses simple keyboard commands and provides instructions to the player.

### Maintainability
The implementation is divided into separate modules for board management, movement, display, game state and tile generation.

### Reliability
The program checks for invalid commands and prevents a new tile from being added when an attempted movement does not change the board.

### Resource Efficiency
The game operates on a small 4 × 4 matrix and uses simple Python operations, keeping computational and memory requirements low.

## Limitations

- The current version is command-line based.
- The game does not store persistent player scores.
- There is no graphical user interface.
- There is no database or external storage.

## Future Enhancements

- Graphical user interface
- High-score persistence
- Undo functionality
- Improved automated test coverage
- Different board sizes
- Additional game statistics
- Save and resume functionality

## Author

Developed as a VITyarthi Build Your Own Project using Python.