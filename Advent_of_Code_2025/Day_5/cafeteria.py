import argparse

def cafeteria_part1(input_path: str) -> int:
    with open(input_path) as f:
        prod_ranges = []
        prod_ids = []
        for line in f:
            line = line.strip()
            if "-" in line:
                prod_ranges.append(line)
            elif line == "":
                continue
            else:
                prod_ids.append(line)

        n_fresh_prods = 0
        # Loop through all the products
        for p in prod_ids:
            is_fresh = False
            p = int(p)
            # Loop through all the product ranges
            for p_range in prod_ranges:
                start, end = p_range.split("-")
                start, end = int(start), int(end)
                if p >= start and p <= end:
                    is_fresh = True
                    break
            if is_fresh: n_fresh_prods += 1

    return n_fresh_prods

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to input file")
    args = parser.parse_args()
    input_path = args.input
    
    part_1_res = cafeteria_part1(input_path)
    print("Part 1: ", part_1_res)

    # part_2_res = lobby_part2(input_path)
    # print("Part 2: ", part_2_res)

if __name__ == "__main__":
    main()