# Project Design

## 1. Basic Architecture

The project is divided into different Python files. Each file handles a particular part of the game.

```text
                         main.py
                    Main Game Program
                           |
        -----------------------------------------
        |              |             |           |
        v              v             v           v
    board.py      display.py    game_state.py  movement.py
        |              |             |           |
        v              |             |           v
     Board             |             |        Move/Merge
                       |             |           |
                       |             |           v
                       |             |        tiles.py
                       |             |       New Tiles
                       |
                       v
                    Display

                  score.py
                Score Function

              test_movement.py
                Movement Test