import argparse

# def find_duplicates(curr_number: str):
#     print("-- New number", curr_number)
#     found = False
#     for i in range(1, (len(curr_number) // 2) + 1):
#         # print(curr_number[0:i])
#         curr_subseq = curr_number[0: i]
#         start = i
#         end = start + i
#         next_sub = curr_number[start: end]
#         if len(curr_number) % i == 0:
#             while end <= len(curr_number):
#                 if curr_subseq != curr_number[start: end]:
#                     break
#                 if end == len(curr_number):
#                     found = True
#                 start += i
#                 end += i
#     return curr_number if found else None

def find_duplicates(curr_number: str) -> int:
    if len(curr_number) % 2 != 0:
        return 0
    mid = len(curr_number) // 2
    first_half = curr_number[0: mid]
    second_half = curr_number[mid: len(curr_number)]

    return int(curr_number) if first_half == second_half else 0

def gift_shop_part1(input_path: str) -> int:
    with open(input_path) as f:
        input_ranges = f.readline().strip()
        # Split to obtain all the ranges
        ranges = input_ranges.split(",")
        sum_invalid_id = 0
        # loop though each of the ranges and check for invalid IDs
        for r in ranges:
            start_r, end_r = r.split("-")
            start_r, end_r = int(start_r), int(end_r)
            
            # Loop through each value between the start and end ranges values and check for repetitions
            curr = start_r
            while curr <= end_r:
                # print(str(curr))
                sum_invalid_id += find_duplicates(str(curr))
                curr += 1

    return sum_invalid_id

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "input",
        help="Path to input file"
    )
    args = parser.parse_args()
    input_path = args.input

    # input_path = "/Users/alessandrocaula/Documents/Devs/Git-Repos/ProgrammingAlgoAndChallenges/Advent_of_Code_2025/Day_2/input_test.txt"

    # Part 1 result
    part_1_res = gift_shop_part1(input_path)
    print("Part 1: ", part_1_res)

    # test = "123456"
    # print(test[0: len(test) // 2])
    # print(test[len(test) // 2: len(test)])

if __name__ == "__main__":
    main() 