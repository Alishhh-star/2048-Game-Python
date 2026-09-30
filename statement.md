# Project Statement

## Project Title

2048 Game

## Problem Statement

Many simple puzzle games are implemented using graphical interfaces without exposing the underlying programming logic clearly. This project aims to develop a modular, command-line version of the 2048 puzzle game using Python.

The project provides a 4 × 4 grid in which the player moves numbered tiles using keyboard commands. Matching tiles are merged during movement, and the player continues making moves until the 2048 tile is created or no valid moves remain.

The project demonstrates the application of programming concepts such as lists, loops, conditional statements, functions, modular programming, matrix manipulation, random number generation, input handling and testing.

## Scope of the Project

The scope of the project includes:

- Creating and managing a 4 × 4 game board
- Generating new tiles
- Moving tiles in four directions
- Compressing and merging matching tiles
- Calculating the score gained from moves
- Displaying the current game board
- Checking the current game state
- Detecting win and loss conditions
- Restarting and quitting the game
- Handling invalid user commands
- Testing movement functionality

The project is implemented as a command-line Python application.

## Target Users

The project is intended for:

- Students learning Python programming
- Beginners interested in understanding game logic
- Users who want to play a simple command-line puzzle game
- Learners interested in modular programming and matrix-based algorithms

## High-Level Features

### 1. Board Management

The game creates a 4 × 4 matrix and initializes the game with a new tile.

### 2. Tile Generation

A new tile with a value of 2 or 4 is placed in an empty position on the board.

### 3. Tile Movement

The player can move tiles:

- Up
- Down
- Left
- Right

### 4. Tile Compression and Merging

Tiles are compressed toward the selected direction. Matching adjacent tiles are merged and their values are doubled.

### 5. Score Management

The game keeps track of the score gained from successful tile merges.

### 6. Game State Management

The game checks whether:

- The player has created the 2048 tile.
- Empty cells are still available.
- Valid merges or moves remain.
- The game has been lost.

### 7. User Interface

The command-line interface displays the board, score, highest tile and available commands.

### 8. Game Controls

The player can restart the game using `R` and quit using `Q`.

### 9. Testing

A separate test file is included to test movement functionality.

## Expected Outcome

The final system should provide a playable command-line 2048 game with modular source code, clear user interaction and separate components for board management, tile handling, movement, display, game-state checking and testing.