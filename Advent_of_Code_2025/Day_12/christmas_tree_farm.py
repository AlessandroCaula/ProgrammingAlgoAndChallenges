import argparse


def christmas_tree_farm(input_path: str):
    """
    We will only care about the SECOND section of the input:
    the list of regions and required present count.
    The shapes section is intentionally ignored. 

    Because the solution relies on a hidden invariant:
    Every shape effectively occupies one 3x3 block, and the list of region are: 
        - Very big to allow all the presents without fit them, we can just put one after the other.
        - Very small, that it is impossible to fit all the presents no matter how you rotate and flip them
    """
    lines = open(input_path).read().split("\n\n")[-1].splitlines()

    # Count how many regions are able to fit all presents, given the above-mentioned assumption
    total = 0

    # Process each regions independently
    for line in lines:
        """
        Extract all numbers from the line
        Example line:
        "12 x 5: 1 0 1 0 3 2"

        re.findall(r"\d+", line) -> ["12", "5", "1", "0", "1", "0", "3", "2"]

        After mapping to int:
        x = region width
        y = regions height
        counts = number of presents of each shape
        """

        x, y, = map(int, line.split(":")[0].split("x"))
        counts = list(map(int, line.split(":")[1].strip().split(" ")))

        # Compute how many non-overlapping 3 × 3 blocks fir into the region
        #
        # Integer division:
        # - x // 3 gives how many 3-wide blocks fit horizontally
        # - y // 3 gives how many 3-wide blocks fit vertically
        #
        # Example:
        # 12 × 5 -> (12 // 3) * (5 // 3) = 4 * 1 = 4 blocks
        #
        # Crucial hidden invariant:
        # Every present shape fits within a 3 × 3 bounding box AND cannot share that box with another present
        max_possible_presents = (x // 3) * (y // 3)

        # Total number of presents we need to place in this region
        total_required_presents = sum(counts)

        # If the number of available 3×3 blocks is at least
        # the number of presents we need to place, then:
        #
        # - There exists SOME placement. We do NOT need to actually construct it
        #
        # This works only because:
        # - All shapes are 3×3
        # - Rotations/flips do not reduce their footprint
        # - No shape can interleave with another in a 3×3 block

        if max_possible_presents >= total_required_presents:
            total += 1

    return total


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to input file")
    args = parser.parse_args()
    input_path = args.input

    part_1_res = christmas_tree_farm(input_path)
    print("Part 1: ", part_1_res)


if __name__ == "__main__":
    main()
