import argparse

def movie_theater_part1(input_path: str):
    red_tiles_pos = []
    with open(input_path) as f:
        for line in f:
            line = line.strip()
            x, y = map(int, line.split(","))
            red_tiles_pos.append([x, y])
    
    biggest_square = 0
    for t1 in range(len(red_tiles_pos)):
        for t2 in range(t1 + 1, len(red_tiles_pos)):
            x1 = red_tiles_pos[t1][0] 
            x2 = red_tiles_pos[t2][0]
            y1 = red_tiles_pos[t1][1]
            y2 = red_tiles_pos[t2][1]
            x_side = abs(x2 - x1) + 1
            y_side = abs(y2 - y1) + 1
            
            curr_rect_area = x_side * y_side

            if curr_rect_area > biggest_square:
                biggest_square = curr_rect_area            

    return biggest_square

def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("input", help="Path to input file")
    # args = parser.parse_args()
    # input_path = args.input

    input_path = "/Users/alessandrocaula/Documents/Devs/Git-Repos/ProgrammingAlgoAndChallenges/Advent_of_Code_2025/Day_9/input_test.txt"
    
    part_1_res = movie_theater_part1(input_path)
    print("Part 1: ", part_1_res)

    # part_2_res = playground_part2(input_path)
    # print("Part 2: ", part_2_res)

if __name__ == "__main__":
    main()