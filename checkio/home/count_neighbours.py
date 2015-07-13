# -*- coding: utf-8 -*-
"""
Created on Nov 28, 2014

@author: lisong
For the first example coordinates of the cell is (1, 2) and as we can see from the schema this cell has 3 neighbour chips. For the second example coordinates is (0, 0) and this cell contains a chip, but we count only neighbours and the answer is 1.
Input: Three arguments. A grid as a tuple of tuples with integers (1/0), a row number and column number for a cell as integers.
Output: How many neighbouring cells have chips as an integer.

Precondition:
3 ≤ len(grid) ≤ 10
all(len(grid[0]) == len(row) for row in grid)
"""


def count_neighbours(grid, row, col):
    """

    :rtype : int
    """
    x0 = row - 1
    y0 = col - 1
    amount = 0

    for i in range(3):
        x = x0 + i
        for j in range(3):
            y = y0 + j
            #             print("[%d][%d]" % (x, y))

            if (x >= 0 and y >= 0) and (x < len(grid) and y < len(grid[0])):
                amount += grid[x][y]
            #                 print("grid[%d][%d]=%d" % (x, y, grid[x][y]))

    amount = amount - grid[row][col]
    return amount


'''
参考
def count_neighbours(grid, row, col):
    rows = range(max(0, row - 1), min(row + 2, len(grid)))
    cols = range(max(0, col - 1), min(col + 2, len(grid[0])))
    
    return sum(grid[r][c] for r in rows for c in cols) - grid[row][col]
'''
if __name__ == '__main__':
    # print сount_neighbours()
    print count_neighbours(((1, 0, 1, 0, 1),
                            (0, 1, 0, 1, 0),
                            (1, 0, 1, 0, 1),
                            (0, 1, 0, 1, 0),
                            (1, 0, 1, 0, 1),
                            (0, 1, 0, 1, 0),), 5, 4)
