import argparse
import math


def movie_theater_part1(input_path: str):
    red_tiles_pos = []
    with open(input_path) as f:
        for line in f:
            line = line.strip()
            x, y = map(int, line.split(","))
            red_tiles_pos.append([x, y])

    biggest_square = -1
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


# def movie_theater_part2(input_path: str):

#     def point_in_polygon(x, y, polygon):
#         inside = False
#         n = len(polygon)

#         for i in range(n):
#             x1, y1 = polygon[i]
#             x2, y2 = polygon[(i + 1) % n]

#             # Check if the edge crosses the horizontal ray at y
#             intersects = ((y1 > y) != (y2 > y))
#             if intersects:
#                 # Compute x-coordinate of intersection
#                 x_intersect = x1 + (y - y1) * (x2 - x1) / (y2 - y1)

#                 if x_intersect > x:
#                     inside = not inside

#         return inside

#     red_tiles_pos = []
#     with open(input_path) as f:
#         for line in f:
#             x, y = map(int, line.strip().split(","))
#             red_tiles_pos.append((x, y))

#     best = 0
#     n = len(red_tiles_pos)

#     for i in range(n):
#         x1, y1 = red_tiles_pos[i]
#         for j in range(i + 1, n):
#             x2, y2 = red_tiles_pos[j]

#             # Rectangle area
#             width = abs(x2 - x1) + 1
#             height = abs(y2 - y1) + 1
#             area = width * height

#             if area <= best:
#                 continue

#             # Rectangle center
#             cx = (x1 + x2) / 2
#             cy = (y1 + y2) / 2

#             if point_in_polygon(cx, cy, red_tiles_pos):
#                 best = area

#     return best


def movie_theater_part2(input_path: str):
    red_tiles_pos = []
    min_x = float("inf")
    min_y = float("inf")
    max_x = float("-inf")
    max_y = float("-inf")
    with open(input_path) as f:
        for line in f:
            line = line.strip()
            x, y = map(int, line.split(","))
            red_tiles_pos.append([x, y])
            if x < min_x:
                min_x = x
            if y < min_y:
                min_y = y
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y

    def fill_contour(validity_matrix, x1, x2, y1, y2):
        # If the x coordinates are the same and the y are not, it means that the tiles are vertically aligned
        if x1 == x2 and y1 != y2:
            x = x1 - min_x
            if y1 < y2:
                for y_idx in range(y1, y2 + 1):
                    y_idx -= min_y
                    validity_matrix[y_idx][x] = "#"
            else:
                for y_idx in range(y2, y1 + 1):
                    y_idx -= min_y
                    validity_matrix[y_idx][x] = "#"
        if y1 == y2 and x1 != x2:
            y = y1 - min_y
            if x1 < x2:
                for x_id in range(x1, x2 + 1):
                    x_id -= min_x
                    validity_matrix[y][x_id] = "#"
            else:
                for x_id in range(x2, x1 + 1):
                    x_id -= min_x
                    validity_matrix[y][x_id] = "#"

    # Build the validity matrix
    validity_matrix = [
        ["." for col in range(min_x, max_x + 1)] for row in range(min_y, max_y + 1)
    ]

    # Built the contour of the validity matrix between the red tiles
    for i, tile in enumerate(red_tiles_pos):
        if i == 0:
            prev = tile
            continue
        # Find if the tiles are horizontally or vertically aligned
        x1, y1 = map(int, prev)
        x2, y2 = map(int, tile)
        # Fill the contour of the validity matrix
        fill_contour(validity_matrix, x1, x2, y1, y2)
        prev = tile

    # Last and first tiles contour
    x1, y1 = map(int, red_tiles_pos[0])
    x2, y2 = map(int, red_tiles_pos[len(red_tiles_pos) - 1])
    fill_contour(validity_matrix, x1, x2, y1, y2)

    # Fill the contour
    # for r in range(len(validity_matrix)):
    # start, end = -1, -1
    # for c in range(len(validity_matrix[r])):
    #     curr = validity_matrix[r][c]
    #     if start == -1 and curr == "#":
    #         start = c
    #     elif start != -1 and curr == "#":
    #         end = c

    # for i in range(start, end):
    #     if validity_matrix[r][i] != "#":
    #         validity_matrix[r][i] = "#"

    # start_end = []
    # started = False
    # can_be_closed = False
    # curr_start = -1
    # for c in range(len(validity_matrix[r])):
    #     curr = validity_matrix[r][c]
    #     if not started and curr == "#":
    #         curr_start = c
    #         started = True
    #     if curr == "." and started:
    #         can_be_closed = True
    #     if can_be_closed and curr == "#":
    #         start_end.append([curr_start, c])

    # for start, end in start_end:
    #     for i in range(start, end):
    #         validity_matrix[r][i] = "#"

    # from_to = []
    # started = False
    # for c in range(len(validity_matrix[r])):
    #     curr = validity_matrix[r][c]
    #     if curr == "#" and not started:
    #         started = True

    # for l in validity_matrix:
    #     print(l)

    # biggest_square = -1
    # for t1 in range(len(red_tiles_pos)):
    #     for t2 in range(t1 + 1, len(red_tiles_pos)):
    #         x1 = red_tiles_pos[t1][0]
    #         x2 = red_tiles_pos[t2][0]
    #         y1 = red_tiles_pos[t1][1]
    #         y2 = red_tiles_pos[t2][1]
    #         x_side = abs(x2 - x1) + 1
    #         y_side = abs(y2 - y1) + 1

    #         curr_rect_area = x_side * y_side

    #         if curr_rect_area > biggest_square:
    #             # Check if the square is in a valid position
    #             # Find all the corner of the rectangle
    #             if curr_rect_area == 50:
    #                 min_x = min(x1, x2)
    #                 max_x = max(x1, x2)
    #                 min_y = min(y1, y2)
    #                 max_y = max(y1, y2)
    #                 print(min_x, min_y)

    #             biggest_square = curr_rect_area

    return -1


def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("input", help="Path to input file")
    # args = parser.parse_args()
    # input_path = args.input

    input_path = "/Users/alessandrocaula/Documents/Devs/Git-Repos/ProgrammingAlgoAndChallenges/Advent_of_Code_2025/Day_9/input_test.txt"

    part_1_res = movie_theater_part1(input_path)
    print("Part 1: ", part_1_res)

    part_2_res = movie_theater_part2(input_path)
    print("Part 2: ", part_2_res)


if __name__ == "__main__":
    main()
