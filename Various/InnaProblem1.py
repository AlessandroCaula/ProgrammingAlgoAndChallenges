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