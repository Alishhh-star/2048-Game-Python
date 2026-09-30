from game2048.tiles import add_new_2

def start_game():
    mat = []

    for i in range(4):
        mat.append([0] * 4)

   

    add_new_2(mat)

    return mat
