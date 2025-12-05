import argparse

def lobby(input_path: str) -> int:
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

            max_pack_joltage = int(bank[tenth_max_idx] + bank[unit_max_idx])
            tot_output_joltage += max_pack_joltage

        return tot_output_joltage


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to input file")
    args = parser.parse_args()
    input_path = args.input

    part_1_res = lobby(input_path)
    print("Part 1: ", part_1_res)

if __name__ == "__main__":
    main()
