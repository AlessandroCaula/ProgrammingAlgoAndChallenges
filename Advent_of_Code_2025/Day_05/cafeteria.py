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

def cafeteria_part2(input_path: str) -> int:
    with open(input_path) as f:
        prod_ranges = []
        for line in f:
            line = line.strip()
            if "-" in line:
                prod_ranges.append(line)
        
        # Sort the products by their first value of the range
        sorted_prod = sorted(prod_ranges, key=lambda x: int(x.split("-")[0]))

        tot_fresh_prod = 0
        for i in range(len(sorted_prod)):
            if i == 0:
                prev_start = int(sorted_prod[i].split("-")[0])
                prev_end = int(sorted_prod[i].split("-")[1])
                continue

            curr_start = int(sorted_prod[i].split("-")[0])
            curr_end = int(sorted_prod[i].split("-")[1])

            if i == len(sorted_prod) - 1:
                if curr_start > prev_end:
                    tot_fresh_prod += curr_end - curr_start + 1
                else:
                    tot_fresh_prod += curr_end - prev_start + 1

            if curr_start > prev_end:
                tot_fresh_prod += prev_end - prev_start + 1
                prev_start = curr_start
                prev_end = curr_end
            else:
                if curr_end > prev_end:
                    prev_end = curr_end
                        
        return tot_fresh_prod

def cafeteria_part2_polished(input_path: str) -> int:
    with open(input_path) as f:
        ranges = []
        for line in f:
            line = line.strip()
            if "-" in line:
                a, b = line.split("-")
                ranges.append((int(a), int(b)))

    # Sort by start
    ranges.sort()

    total = 0
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end:
            # overlap → extend the merged interval if needed
            current_end = max(current_end, end)
        else:
            # no overlap → finalize previous interval
            total += current_end - current_start + 1
            current_start, current_end = start, end

    total += current_end - current_start + 1
    return total

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to input file")
    args = parser.parse_args()
    input_path = args.input
    
    part_1_res = cafeteria_part1(input_path)
    print("Part 1: ", part_1_res)

    part_2_res = cafeteria_part2(input_path)
    print("Part 2: ", part_2_res)

    part_2_res = cafeteria_part2_polished(input_path)
    print("Part 2: ", part_2_res)

if __name__ == "__main__":
    main()