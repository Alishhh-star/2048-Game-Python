from game2048 import board
from game2048 import tiles
from game2048 import game_state
from game2048 import movement
from game2048 import display


def new_game():
    """Start a new game."""
    return board.start_game()


# Start the game
mat = new_game()
score = 0

display.display_instructions()

while True:
    # Display the current board
    display.print_board(mat)

    print("Score:", score)
    print("Highest Tile:", display.get_highest_tile(mat))

    status = game_state.get_current_state(mat)

    # Check game status
    if status == "WON":
        print()
        print("=" * 36)
        print(" CONGRATULATIONS!")
        print(" YOU WON!")
        print("=" * 36)
        print("Final Score:", score)
        break

    elif status == "LOST":
        print()
        print("=" * 36)
        print(" GAME OVER!")
        print("=" * 36)
        print("Final Score:", score)
        break

    # Take command from the player
    x = input("\nEnter your command: ").strip()

    # Quit
    if x == 'Q' or x == 'q':
        print()
        print("Thanks for playing 2048!")
        print("Final Score:", score)
        break

    # Restart
    elif x == 'R' or x == 'r':
        mat = new_game()
        score = 0
        print("\nNew game started!")
        continue

    # Save old board for score calculation
    old_mat = [row[:] for row in mat]

    # Movement commands
    if x == 'W' or x == 'w':
        mat, flag, gained = movement.move_up(mat)

    elif x == 'S' or x == 's':
        mat, flag, gained = movement.move_down(mat)

    elif x == 'A' or x == 'a':
        mat, flag, gained = movement.move_left(mat)

    elif x == 'D' or x == 'd':
        mat, flag, gained = movement.move_right(mat)

    else:
        print("Invalid command! Please use W, A, S, D, R or Q.")
        continue

    # Add a new tile only if the board actually changed
    if flag:
        score += gained
        tiles.add_new_2(mat)

    else:
        print("That move cannot be made. Try another direction.")
