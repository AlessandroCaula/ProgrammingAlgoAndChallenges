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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to input file")
    args = parser.parse_args()
    input_path = args.input

    # input_path = "/Users/alessandrocaula/Documents/Devs/Git-Repos/ProgrammingAlgoAndChallenges/Advent_of_Code_2025/Day_7/input_test.txt"
    
    part_1_res = laboratories_part1(input_path)
    print("Part 1: ", part_1_res)

if __name__ == "__main__":
    main()