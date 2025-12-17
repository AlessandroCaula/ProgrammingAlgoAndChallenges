import argparse


def factory_part1(input_path: str):
    light_diagram = []
    buttons = []
    with open(input_path) as f:
        for line in f:
            line = line.strip().split(" ")
            diagram = list(line[0][1: len(line[0]) - 1])
            light_diagram.append(diagram)
            curr_btns = []
            for btn in line[1: len(line) - 1]:
                btn_set = set(map(int, btn[1: len(btn) - 1].split(",")))
                curr_btns.append(btn_set)
            buttons.append(curr_btns)

    print(light_diagram)
    print(buttons)

    return -1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to input file")
    args = parser.parse_args()
    input_path = args.input

    # input_path = "/Users/alessandrocaula/Documents/Devs/Git-Repos/ProgrammingAlgoAndChallenges/Advent_of_Code_2025/Day_9/input.txt"

    part_1_res = factory_part1(input_path)
    print("Part 1: ", part_1_res)

    # part_2_res = factory_part2(input_path)
    # print("Part 2: ", part_2_res)


if __name__ == "__main__":
    main()
