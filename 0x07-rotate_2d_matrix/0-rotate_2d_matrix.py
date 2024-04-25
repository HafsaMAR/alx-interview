#!/usr/bin/env python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotate a given n x n 2D matrix by 90 degrees clockwise."""
    for i, row in enumerate(zip(*matrix[::-1])):
        matrix[i] = list(row)


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_2d_matrix(matrix)
    print(matrix)
