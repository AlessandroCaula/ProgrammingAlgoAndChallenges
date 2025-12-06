import argparse

def printing_department_part1(input_path: str) -> int:
    with open(input_path) as f:
        rolls_grid = []
        for line in f:
            line = line.strip()
            rolls_grid.append(list(line))
        n_rows = len(rolls_grid)
        n_cols = len(rolls_grid[0])
        rolls_to_remove = 0

        # Now loop through all the positions and check if there are less than 4 paper rolls (@)
        moves = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
        for r in range(len(rolls_grid)):
            for c in range(len(rolls_grid[r])):
                curr_pos = rolls_grid[r][c]
                if curr_pos == ".":
                    continue
                
                # Loop through each of the moves
                tot_neighbors = 0
                for move in moves:
                    n_r, n_c = r + move[0], c + move[1]
                    
                    # Check if it goes out of the grid
                    if n_r < 0 or n_c < 0 or n_r >= n_rows or n_c >= n_cols:
                        continue
                    
                    # Count how many papers are around
                    if rolls_grid[n_r][n_c] == "@":
                        tot_neighbors += 1                

                # If there are fewer than 4 papers around, remove the current paper
                if tot_neighbors < 4:
                    rolls_to_remove += 1

    return rolls_to_remove

def printing_department_part2(input_path: str) -> int:
    with open(input_path) as f:
        rolls_grid = []
        for line in f:
            line = line.strip()
            rolls_grid.append(list(line))
        n_rows = len(rolls_grid)
        n_cols = len(rolls_grid[0])
        rolls_to_remove = 0

        keep_removing = True
        while keep_removing:
            keep_removing = False

            # Loop through all the positions and check if there are less than 4 paper rolls (@)
            moves = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]

            for r in range(len(rolls_grid)):
                for c in range(len(rolls_grid[r])):
                    curr_pos = rolls_grid[r][c]
                    if curr_pos == ".":
                        continue
                    
                    # Loop through each of the moves
                    tot_neighbors = 0
                    for move in moves:
                        n_r, n_c = r + move[0], c + move[1]

                        # Check if it goes out of the grid
                        if n_r < 0 or n_c < 0 or n_r >= n_rows or n_c >= n_cols:
                            continue
                        
                        # Count how many papers are around
                        if rolls_grid[n_r][n_c] == "@":
                            tot_neighbors += 1               

                    # If there are fewer than 4 papers around, remove the current paper
                    if tot_neighbors < 4:
                        rolls_to_remove += 1
                        rolls_grid[r][c] = "."
                        keep_removing = True

    return rolls_to_remove

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to input file")
    args = parser.parse_args()
    input_path = args.input

    part1_res = printing_department_part1(input_path)
    print("Part 1:", part1_res)

    part2_res = printing_department_part2(input_path)
    print("Part 2:", part2_res)

if __name__ == "__main__":
    main()