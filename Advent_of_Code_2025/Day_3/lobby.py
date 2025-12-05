import argparse

def lobby_part1(input_path: str) -> int:
    with open(input_path) as banks:
        tot_output_joltage = 0
        for bank in banks:
            bank = bank.strip()

            # Loop through all the numbers of the battery
            tenth_max_idx, unit_max_idx = -1, -1
            # First find the higher tenth
            max_tenth = -1
            for i, el in enumerate(bank):
                el = int(el)
                if el > max_tenth:
                    # It cannot be the last one
                    if i != len(bank) - 1:
                        max_tenth = el
                        tenth_max_idx = i
            max_unit = -1
            for j, el in enumerate(bank):
                el = int(el)
                if j > tenth_max_idx:
                    if el > max_unit:
                        max_unit = el
                        unit_max_idx = j

            # # --- Solution using python logic
            # best_first = max(bank[:-1])
            # i = bank.index(best_first)
            # best_second = max(bank[i+1:])
            # return int(best_first + best_second)

            max_pack_joltage = int(bank[tenth_max_idx] + bank[unit_max_idx])
            tot_output_joltage += max_pack_joltage

        return tot_output_joltage

def lobby_part2(input_path: str) -> int:
    with open(input_path) as banks:
        tot_output_joltage = 0
        for bank in banks:
            bank = bank.strip()
            twelve_batteries = ""
            start = 0
            for i in range(12)[::-1]:
                curr_max = -1
                curr_max_idx = -1
                # Update the end index
                end = len(bank) - i
                # Loop through the start and end range
                for j in range(start, end):
                    if int(bank[j]) > curr_max:
                        curr_max = int(bank[j])
                        curr_max_idx = j
                # Save the current maximum
                twelve_batteries += bank[curr_max_idx]
                # Updated the new start for the next iteration
                start = curr_max_idx + 1
            # print(twelve_batteries)
            tot_output_joltage += int(twelve_batteries)

    return tot_output_joltage

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to input file")
    args = parser.parse_args()
    input_path = args.input

    part_1_res = lobby_part1(input_path)
    print("Part 1: ", part_1_res)

    part_2_res = lobby_part2(input_path)
    print("Part 2: ", part_2_res)

if __name__ == "__main__":
    main()
