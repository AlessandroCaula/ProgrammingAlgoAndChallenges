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

    tot_presses = 0
    # Loop through all the machines diagrams
    for i in range(len(light_diagram)):
        curr_buttons = buttons[i]
        # Loop through all the subset dimensions of the buttons and check all the possible combinations of buttons clicks
        n = len(curr_buttons)
        min_n_presses = float("inf")
        # Iterate over all possible subset of buttons.
        # There are 2^n subsets, represented by numbers from 0 to (2^n - 1)
        for mask in range(1 << n):
            pressed_buttons = []
            # Check each button index
            for j in range(n):
                # (1 << i) is a number where only bit i is set
                # Example: i = 2 -> 1 << 2 - 0b100
                # mask & (1 << i) checks:
                # "Is the i-th bit of mask equal to 1?"
                # If yes, button i is included in this subset
                if mask & (1 << j):
                    pressed_buttons.append(curr_buttons[j])

            # Now I can check for all the combinations of button clicks the resulting diagram
            start_diagram = ["." for _ in range(len(light_diagram[i]))]
            for button in pressed_buttons:
                # For each button press combination switch on/off the light
                for btn in button:
                    if start_diagram[btn] == ".":
                        start_diagram[btn] = "#"
                    else:
                        start_diagram[btn] = "."

            if start_diagram == light_diagram[i]:
                if len(pressed_buttons) < min_n_presses:
                    min_n_presses = len(pressed_buttons)

                    if min_n_presses == 1:
                        break

        tot_presses += min_n_presses

    return tot_presses


def factory_part2(input_path: str):
    buttons = []
    joltage_levels = []
    with open(input_path) as f:
        for line in f:
            line = line.strip().split(" ")
            # Store the joltage values
            jlt = line[len(line) - 1]
            joltage = list(map(int, jlt[1: len(jlt) - 1].split(",")))
            joltage_levels.append(joltage)
            # Store the buttons
            curr_btns = []
            for btn in line[1: len(line) - 1]:
                btn_set = set(map(int, btn[1: len(btn) - 1].split(",")))
                curr_btns.append(btn_set)
            buttons.append(curr_btns)

    # Loop through all the machines
    for i in range(len(joltage_levels)):
        # print(joltage_levels[i])
        # print(buttons[i])
        target_joltage = joltage_levels[i]
        curr_buttons = buttons[i]
        # Check for each of the joltage levels if there are some buttons position equal to 0. They cannot be touched
        do_not_press = []
        for j, pos in enumerate(target_joltage):
            if pos == 0:
                do_not_press.append(j)
        # Remove the buttons combinations that includes the button that cannot be pressed
        for btn_comb in curr_buttons:
            for btn in btn_comb:
                if btn in do_not_press:
                    curr_buttons.remove(btn_comb)

        pos_presses_map = {}
        for j, press in enumerate(target_joltage):
            pos_presses_map[j] = press

        # Sort the mapped buttons and number of presses by press times
        pos_presses_map = dict(sorted(
            pos_presses_map.items(), key=lambda item: item[1]
        ))
        # Sort the button combinations by length
        curr_buttons = sorted(curr_buttons, key=lambda x: len(x), reverse=True)
        # print(curr_buttons)

        curr_joltage = [0 for _ in range(len(target_joltage))]
        # print(curr_joltage)
        # print(target_joltage)
        # Loop for each button and relative number of presses
        # for btn, presses in pos_presses_map.items():
        # Loop through all the button combinations


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to input file")
    args = parser.parse_args()
    input_path = args.input

    # input_path = "/Users/alessandrocaula/Documents/Devs/Git-Repos/ProgrammingAlgoAndChallenges/Advent_of_Code_2025/Day_10/input_test.txt"

    # part_1_res = factory_part1(input_path)
    # print("Part 1: ", part_1_res)

    part_2_res = factory_part2(input_path)
    print("Part 2: ", part_2_res)


if __name__ == "__main__":
    main()
