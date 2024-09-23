matrix_well = []

for row in range(4):
    new_row = []
    for col in range(480):
        new_row.append(col)
    matrix_well.append(new_row)


print("Rows: ", len(matrix_well), "Col: ", len(matrix_well[0]))


#for i, row in enumerate(matrix_well):
#    counter = 0
#    increased = False
#    for j, col in enumerate(matrix_well[i]):
#        initial_val = (i + 1) * 40 * counter 
#        final_val = ((i + 1) * 40 * counter) + 40
#        if j >= ((i + 1) * 40 * counter) and j < ((i + 1) * 40 * counter) + 40:
#            matrix_well[i][j] ="prova"
#            increased = False
#        else:
#            if increased == False:
#                counter += len(matrix_well)
#                increased = True

# for i, row in enumerate(matrix_well):
#     for j, col in enumerate(matrix_well[i]):
#         if 