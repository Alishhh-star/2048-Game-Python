from game2048.movement import move_left


mat = [
    [2, 2, 0, 0],
    [0, 0, 0, 0],
    [4, 4, 0, 0],
    [2, 0, 2, 0]
]

new_mat, changed, score = move_left(mat)

print("Testing move_left()")

print("Changed:", changed)
print("Score:", score)
print("New Board:")

for row in new_mat:
    print(row)
