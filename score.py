def calculate_score(old_mat, new_mat):
    """Calculate the score gained from a move."""
    score = 0

    for i in range(4):
        for j in range(4):
            if new_mat[i][j] > old_mat[i][j]:
                difference = new_mat[i][j] - old_mat[i][j]
                score += difference

    return score
