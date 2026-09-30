import random

def findEmpty(mat):
    """Finds the first empty (0) cell in the grid."""
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return i, j

    return None, None


def add_new_2(mat):
    """Adds a new '2' or '4' in a random empty cell in the grid."""
    if all(all(cell != 0 for cell in row) for row in mat):
        return

    tries = 0

    while tries < 30:
        r = random.randint(0, 3)
        c = random.randint(0, 3)

        if mat[r][c] == 0:
            if random.random() < 0.9:
                mat[r][c] = 2
            else:
                mat[r][c] = 4
            return

        tries += 1

    r, c = findEmpty(mat)

    if r is not None and c is not None:
        mat[r][c] = 2
