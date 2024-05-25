#!/usr/bin/python3

def compute_matrix(matrix=[]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j] ** 2
    return matrix

if __name__ == "__main__":
    matrix = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    print(f"Original: {matrix}")
    print(f"Modified: {compute_matrix(matrix)}")





