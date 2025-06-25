###################
## Spiral Matrix ##
###################

# Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order. 
#
# Examples
#
# spiralOrder([
#   [ 1, 2, 3 ],
#   [ 4, 5, 6 ],
#   [ 7, 8, 9 ]
# ])
# output = [1, 2, 3, 6, 9, 8, 7, 4, 5]
#
# spiralOrder([
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ])
# output = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

def spiralOrder(matrix):
    r_idx, c_idx = 0, 0
    increment_row, increment_col = 1, 1
    read_row, read_col = True, False
    visited_row, visited_col = [], []
    res = []

    if not matrix:
        return res

    # Loop through all the elements in the matrix
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):

            res.append(matrix[r_idx][c_idx])

            # Read rows, col by col in both "directions"
            if read_row:
                if c_idx < len(matrix[r_idx]) - 1 and (c_idx != 0 or r_idx == 0) and ((c_idx + (1 * increment_col)) not in visited_col):
                    c_idx += (1 * increment_col)
                else: 
                    visited_row.append(r_idx)
                    r_idx += (1 * increment_row)
                    read_row = False
                    increment_col *= -1
            # Read cols, row by row in both "directions"
            else:
                if r_idx < len(matrix) - 1 and r_idx >= 0 and ((r_idx + (1 * increment_row)) not in visited_row):
                    r_idx += (1 * increment_row)
                else: 
                    visited_col.append(c_idx)
                    c_idx += (1 * increment_col)
                    read_row = True
                    increment_row *= -1
    return res


# matrix = [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]

matrix = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]

# matrix = [
#   [ 1, 2 ],
#   [ 4, 5 ],
#   [ 7, 8 ]
# ]

# matrix = [
#   [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ],
#   [ 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 ],
#   [ 20, 21, 22, 23, 24, 25, 26, 27, 28, 29 ],
# ]

print(spiralOrder(matrix))


#######################
## STANDARD APPROACH ##
#######################

def spiralOrder1(matrix):
    res = []

    if not matrix:
        return res

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while left <= right and top <= bottom:
        for c in range(left, right + 1):
            res.append(matrix[top][c])
        top += 1
        for r in range(top, bottom + 1):
            res.append(matrix[r][right])
        right -=1

        if top <= bottom:
            for c in range(right, left - 1, -1):
                res.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):
                res.append(matrix[r][left])
            left += 1

    return res

# matrix = [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]

matrix = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]

# matrix = [
#   [ 1, 2 ],
#   [ 4, 5 ],
#   [ 7, 8 ]
# ]

# matrix = [
#   [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ],
#   [ 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 ],
#   [ 20, 21, 22, 23, 24, 25, 26, 27, 28, 29 ],
# ]

print(spiralOrder1(matrix))