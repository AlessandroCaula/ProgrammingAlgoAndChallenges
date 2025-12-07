import argparse

def trash_compactor_part1(input_path):
    with open(input_path) as f:
        numbers = []
        operations = []
        for line in f:
            line = line.strip()
            line = [l for l in line.split(" ") if l != ""]
            if "+" in line:
                operations = [o for o in line]
            else:
                numbers.append(line)

    n_col = len(numbers[0])
    tot_col = []
    for c in range(n_col):
        # Retrieve the operation
        operation = operations[c]
        curr_res = 0 if operation == "+" else 1
        for r in range(len(numbers)):
            if operation == "+":
                curr_res += int(numbers[r][c])
            else:
                curr_res *= int(numbers[r][c])
        tot_col.append(curr_res)
    
    return sum(tot_col)

def trash_compactor_part2(input_path):
    with open(input_path) as f:
        numbers = []
        operations = []
        for line in f:
            if "+" in line:
                line = line.strip()
                line = [l for l in line.split(" ") if l != ""]
                operations = [o for o in line]
            else:
                line = [l for l in list(line) if l != '\n']
                numbers.append(line)    
    
    # Extract the numbers to be added or multiplied
    tot_numbers = []
    group_numbers = []
    for c in range(len(numbers[0])):
        col_number = ""
        for r in range(len(numbers)):
            if numbers[r][c] != ' ':
                col_number += numbers[r][c]
        if c == len(numbers[0]) - 1:
            group_numbers.append(col_number)
            tot_numbers.append(group_numbers)
        elif col_number == "":
            tot_numbers.append(group_numbers)
            group_numbers = []
        else:
            group_numbers.append(col_number)
    
    # Compute the operations
    group_results = []
    for i, group in enumerate(tot_numbers):
        curr_res = 0 if operations[i] == "+" else 1
        for n in group:
            if operations[i] == "+":
                curr_res += int(n)
            else:
                curr_res *= int(n)
        group_results.append(curr_res)

    return sum(group_results)

def trash_compactor_part2_GPT(path):
    grid = [list(line.rstrip("\n")) for line in open(path)]
    
    # Last line contains the operations
    ops_row = grid[-1]
    data_grid = grid[:-1]
    
    width = len(ops_row)
    
    # Identify separator columns (all spaces)
    def is_blank_col(c):
        return all(row[c] == " " for row in data_grid)
    
    # Split the column indices into groups based on blank columns
    groups = []
    current = []
    
    for c in range(width):
        if is_blank_col(c):
            if current:
                groups.append(current)
                current = []
        else:
            current.append(c)
    if current:
        groups.append(current)
    
    total = 0
    
    # Process each group
    for cols in groups:
        # Operator comes from any of the columns in this group (same operator across them)
        op = ops_row[cols[0]]
        values = []
        
        # Build one number per column in the group
        for c in cols:
            digits = [row[c] for row in data_grid if row[c] != " "]
            num = int("".join(digits))
            values.append(num)
        
        if op == "+":
            res = sum(values)
        else:
            res = 1
            for v in values:
                res *= v
        
        total += res
    
    return total

def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("input", help="Path to input file")
    # args = parser.parse_args()
    # input_path = args.input
    
    # part_1_res = trash_compactor_part1(input_path)
    # print("Part 1: ", part_1_res)
    
    # part_2_res = trash_compactor_part2(input_path)
    # print("Part 2: ", part_2_res)

    input_path = "/Users/alessandrocaula/Documents/Devs/Git-Repos/ProgrammingAlgoAndChallenges/Advent_of_Code_2025/Day_6/input_test.txt"
    
    part_2_res = trash_compactor_part2_GPT(input_path)
    print("Part 2: ", part_2_res)

if __name__ == "__main__":
    main()