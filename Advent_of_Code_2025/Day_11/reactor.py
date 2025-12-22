import argparse
from functools import cache


def reactor_part1(input_path: str):
    starting_devices = {}
    dev_point_to = {}
    with open(input_path) as f:
        i = 0
        for line in f:
            curr_dev_point_to = []
            line = line.strip()
            start_device, point_to = line.split(":")
            starting_devices[start_device.strip()] = i
            dev_point_to[i] = [d.strip()
                               for d in point_to.strip().split(" ")]
            i += 1

    # Find the starting point, which is the 'you'
    starting_point_idx = starting_devices['you']

    # From the starting point build all the possible path that will reach to 'out'
    queue = [(el, {el}) for el in dev_point_to[starting_point_idx]]

    # While the queue is not empty, loop through all the devices connected to the current one
    paths_count = 0
    while len(queue) != 0:
        curr_dev, visited_in_path = queue.pop()

        # Check the current device where it brings to and, if is has not been yest visited, then add it to queue and visited nodes
        curr_dev_idx = starting_devices[curr_dev]
        dev_to = dev_point_to[curr_dev_idx]

        # Loop through all the dev_to
        for device in dev_to:
            # If the device is equal to 'out', we have reached a way out, and we increment the path_count
            if device == 'out':
                paths_count += 1
            else:
                # Check if the device has not been visited yet. Add it to the queue and visited devices list
                if device not in visited_in_path:
                    # Copy path for new branch
                    new_path = visited_in_path.copy()
                    new_path.add(device)
                    queue.append((device, new_path))

    return paths_count


def reactor_part2(input_path: str):
    # BUILD GRAPH: Parse input from stdin into adjacency list
    # graph[device_name] = [list, of, connected, devices]
    graph = {}
    for line in open(input_path):
        # Split line into source and destination
        src, dsts = line.strip().split(": ")
        # Split destinations string into list
        graph[src] = dsts.split()

    # MEMOIZED PATH COUNTING FUNCTION
    @cache
    def count(src, dst):
        """
        Count all paths from src to das using dynamic programming

        Base case: if src == dst, we've arrived (1 path: the empty path)
        Recursive case: sum paths through all neighbors

        The @cache decorator stores results so we never compute the same (src, dst) twice
        """
        # BASE CASE: Reached destination
        if src == dst:
            return 1

        # RECURSIVE CASE: Sum paths through all neighbors
        # graph.get(src, []) returns neighbors of src, or empty list if src not in graph
        # Form each neighbor x, count paths from x to dst, then sum them all
        return sum(count(x, dst) for x in graph.get(src, []))

    # Count paths from svr to out that visit both dac and fft
    # Two possible orderings:
    # 1. svr -> dac -> fft -> out (multiply the three segment counts)
    # 2. svr -> fft -> dac -> out (multiply the three segment counts)
    # Add both orderings together for the total
    return (
        count('svr', 'dac') * count('dac', 'fft') * count('fft', 'out')
        + count('svr', 'fft') * count('fft', 'dac') * count('dac', 'out')
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to input file")
    args = parser.parse_args()
    input_path = args.input

    # input_path = "/Users/alessandrocaula/Documents/Devs/Git-Repos/ProgrammingAlgoAndChallenges/Advent_of_Code_2025/Day_11/input_test.txt"

    part_1_res = reactor_part1(input_path)
    print("Part 1: ", part_1_res)

    part_2_res = reactor_part2(input_path)
    print("Part 2: ", part_2_res)


if __name__ == "__main__":
    main()
