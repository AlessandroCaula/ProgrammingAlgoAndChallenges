# Given a matrix M x N extract a window array of m (40) lenght from each of the M rows, shifiting the array every rows.
# i.e. First Row --> array from 0 to 39. Second Row --> array from 40 to 79. Third array --> from 80 to 119. Etc.
# [[[0 .. 39], 40 .. 480], 
#  [0 .. 39, .. [40 .. 79], 80 .. 480], 
#  [0 .. 79, [80 .. 119], 120 .. 480],
#  [0 .. 119, [120 .. 159], 160 .. 480]]


matrix = [[i for i in range(480)] for j in range(4)]
len_array = 40
final_array = []

row = 0
counter = 0 
for col in range(len(matrix[0])):
    if counter < len_array:
        final_array.append(matrix[row][col])
        counter += 1
    else:
        if row == len(matrix) - 1:
            row = 0
            counter = 1
            final_array.append(matrix[row][col])
        else:
            row += 1
            counter = 1
            final_array.append(matrix[row][col])

print(final_array)
print(len(final_array))