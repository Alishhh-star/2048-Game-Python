def display_instructions():
    print("Commands are as follows:")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")
    print("'R' or 'r' : Restart Game")
    print("'Q' or 'q' : Quit Game")


def print_board(mat):
    print()
    print("+------+------+------+------+")

    for i in range(4):
        print("|", end="")

        for j in range(4):
            if mat[i][j] == 0:
                print("      |", end="")
            else:
                print(f"{mat[i][j]:^6}|", end="")

        print()
        print("+------+------+------+------+")

    print()


def get_highest_tile(mat):
    highest = 0

    for i in range(4):
        for j in range(4):
            if mat[i][j] > highest:
                highest = mat[i][j]

    return highest