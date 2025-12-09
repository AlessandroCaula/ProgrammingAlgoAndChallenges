import argparse

def laboratories_part1(input_path: str) -> int:
    diagram = []
    with open(input_path) as f:
        for line in f:
            diagram.append(list(line.strip()))

    # Find Starting beam position
    prev_beams = []
    for i, cell in enumerate(diagram[0]):
        if cell == "S":
            prev_beams.append(i)
            break
    
    # Check where the beam splits.
    n_splits = 0
    for r in range(1, len(diagram)):
        next_beams = []
        for c in prev_beams:
            cell = diagram[r][c]
            if cell == "^":
                # Split the beam
                n_splits += 1
                # left beam
                if c - 1 >= 0 and diagram[r][c - 1] != "^":
                    next_beams.append(c - 1)
                # right beam
                if c + 1 < len(diagram[r]) and diagram[r][c + 1] != "^":
                    next_beams.append(c + 1)
            else:
                # Continue the beam straight down
                next_beams.append(c)

        # Remove duplicates to avoid fake double-beams
        prev_beams = list(set(next_beams))

    return n_splits

def laboratories_part2(input_path: str) -> int:
    diagram = []
    with open(input_path) as f:
        for line in f:
            diagram.append(list(line.strip()))
    
    n_cols = len(diagram[0])

    active_beams = [0] * n_cols

    # Find start position
    start_col = diagram[0].index("S")
    active_beams[start_col] = 1

    for r in range(1, len(diagram)):
        next_beams = [0] * n_cols
        for c, count in enumerate(active_beams):
            if count == 0:
                continue
            if diagram[r][c] == "^":
                # Split left and right
                if c - 1 >= 0:
                    next_beams[c - 1] += count
                if c + 1 < n_cols:
                    next_beams[c + 1] += count
            else:
                # Beam continues straight down
                next_beams[c] += count
        active_beams = next_beams

    return sum(active_beams)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to input file")
    args = parser.parse_args()
    input_path = args.input

    # input_path = "/Users/alessandrocaula/Documents/Devs/Git-Repos/ProgrammingAlgoAndChallenges/Advent_of_Code_2025/Day_7/input_test.txt"
    
    part_1_res = laboratories_part1(input_path)
    print("Part 1: ", part_1_res)

    part_2_res = laboratories_part2(input_path)
    print("Part 2: ", part_2_res)

if __name__ == "__main__":
    main()