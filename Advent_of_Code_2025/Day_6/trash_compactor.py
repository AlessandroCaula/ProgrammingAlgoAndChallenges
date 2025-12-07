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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to input file")
    args = parser.parse_args()
    input_path = args.input
    
    part_1_res = trash_compactor_part1(input_path)
    print("Part 1: ", part_1_res)

if __name__ == "__main__":
    main()