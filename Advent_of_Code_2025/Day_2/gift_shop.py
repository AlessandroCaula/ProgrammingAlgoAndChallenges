import argparse

def find_all_duplicates(curr_number: str):
    found = False
    for i in range(1, (len(curr_number) // 2) + 1):
        curr_subseq = curr_number[0: i]
        start = i
        end = start + i
        next_sub = curr_number[start: end]
        if len(curr_number) % i == 0:
            while end <= len(curr_number):
                if curr_subseq != curr_number[start: end]:
                    break
                if end == len(curr_number):
                    found = True
                start += i
                end += i
    return int(curr_number) if found else 0

def find_twice_duplicates(curr_number: str) -> int:
    if len(curr_number) % 2 != 0:
        return 0
    mid = len(curr_number) // 2
    first_half = curr_number[0: mid]
    second_half = curr_number[mid: len(curr_number)]

    return int(curr_number) if first_half == second_half else 0

def gift_shop_part(input_path: str, is_first_part: bool) -> int:
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
                if (is_first_part):
                    sum_invalid_id += find_twice_duplicates(str(curr))
                else:
                    sum_invalid_id += find_all_duplicates(str(curr))
                curr += 1

    return sum_invalid_id

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("input", help="Path to input file")
    
    args = parser.parse_args()
    input_path = args.input

    # Part 1 result
    part_1_res = gift_shop_part(input_path, is_first_part = True)
    print("Part 1: ", part_1_res)
    
    # Part 2 result
    part_1_res = gift_shop_part(input_path, is_first_part = False)
    print("Part 1: ", part_1_res)

if __name__ == "__main__":
    main() 