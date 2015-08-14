# -*- coding:utf-8 -*-

__author__ = 'lisong'

"""
While traveling, the spaceship endures quite a lot of stress.
As a result, an important part of the maintenance is to check the outer hull.
 Stephan uses a digital durabilitimeter for this task.
 The device scans a portion of the spaceships hull and gives a durability map
 that is divided by small square fragments with measurements.
 Sometimes Stephan does not have much time and he can patch only couple points,
 so we need an algorithm to find the weak points.

The durability map is represented as a matrix with digits. Each number is the durability measurement for the cell.
To find the weakest point we should find the weakest row and column.
The weakest point is placed in the intersection of these rows and columns.
Row (column) durability is a sum of cell durability in that row (column).
You should find coordinates of the weakest point (row and column).
 The first row (column) is 0th row (column).
 If a section has several equal weak points, then choose the top left point.

weak-point

Input: A durability map as a list of lists with integers.

Output: The coordinates of the weak point as a list (tuple) of integers.

Example:

weak_point([[7, 2, 7, 2, 8],
            [2, 9, 4, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5]]) == [3, 3]
weak_point([[7, 2, 4, 2, 8],
            [2, 8, 1, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5]]) == [1, 2]


How it is used:
Matrices (2D array) are an often used data structure and it will be helpful to sharpen your skills with them.

Precondition:
0 < len(matrix) ≤ 10
all(len(row) == len(matrix) for row in matrix)
all(all(0 < x < 10 for x in row) for row in matrix)
"""

def weak_point(matrix):
    row_points = list()
    column_points = list()
    is_first_row = True
    for row in matrix:
        row_points.append(sum(row))
        column_number = 0
        for x in row:
            if is_first_row:
                column_points = row
                continue
            else:
                # print column_number
                column_points[column_number] += x
                column_number += 1
        # print column_points
        is_first_row = False
    x = row_points.index(min(row_points))
    y = column_points.index(min(column_points))
    # print x, y
    # print row_points, column_points
    return x, y  # [0, 0]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"

'''

def weak_point(matrix):
    n = len(matrix)
    row = min(range(n), key=lambda r:sum(matrix[r][c] for c in range(n)))
    col = min(range(n), key=lambda c:sum(matrix[r][c] for r in range(n)))
    return row, col
'''
