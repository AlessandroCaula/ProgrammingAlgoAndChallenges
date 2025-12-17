import math
import argparse
from collections import deque


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

    # Create the mask around the validity geometrical space, if the square then crosses this, it means that is it outside the validity region
    #
    # Add one vertical row to the left and right
    for l in validity_matrix:
        l.insert(0, ".")
        l.append(".")
    new_len = len(validity_matrix[0])
    # Add one horizontal row to the top and button
    validity_matrix.insert(0, ["." for n in range(new_len)])
    validity_matrix.append(["." for n in range(new_len)])

    # Get dimensions
    height = len(validity_matrix)
    width = len(validity_matrix[0])

    # Flood fill from outside to mark tiles outside the polygon
    visited = set()
    queue = deque([(0, 0)])
    visited.add((0, 0))

    while queue:
        x, y = queue.popleft()
        validity_matrix[y][x] = 'O'  # Mark as outside

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if (nx, ny) not in visited and validity_matrix[ny][nx] == '.':
                    visited.add((nx, ny))
                    queue.append((nx, ny))

    # Convert remaining '.' to 'X' (inside the polygon = green)
    for y in range(height):
        for x in range(width):
            if validity_matrix[y][x] == '.':
                validity_matrix[y][x] = '#'

    # Find the largest rectangle with red corners using only red/green tiles
    biggest_area = 0

    for t1 in range(len(red_tiles_pos)):
        for t2 in range(t1 + 1, len(red_tiles_pos)):
            x1 = red_tiles_pos[t1][0]
            x2 = red_tiles_pos[t2][0]
            y1 = red_tiles_pos[t1][1]
            y2 = red_tiles_pos[t2][1]

            # Convert to matrix coordinates (with padding offset of 1)
            mx1 = x1 - min_x + 1
            mx2 = x2 - min_x + 1
            my1 = y1 - min_y + 1
            my2 = y2 - min_y + 1

            min_mx = min(mx1, mx2)
            max_mx = max(mx1, mx2)
            min_my = min(my1, my2)
            max_my = max(my1, my2)

            # Check if all tiles in rectangle are red (#) or green (X)
            valid = True
            for y in range(min_my, max_my + 1):
                for x in range(min_mx, max_mx + 1):
                    if validity_matrix[y][x] not in ['#', 'X']:
                        valid = False
                        break
                if not valid:
                    break

            if valid:
                area = (max_mx - min_mx + 1) * (max_my - min_my + 1)
                biggest_area = max(biggest_area, area)

    return biggest_area


def movie_theater_part2_opt(input_path: str):
    points = []
    with open(input_path) as f:
        for line in f:
            line = line.strip()
            x, y = map(int, line.split(","))
            points.append([x, y])

    # COORDINATE COMPRESSION: Extract unique x and y coordinates and sort them
    # This maps large coordinate ranges to small indices (e.g. [2, 100, 500] -> [0, 1, 2])
    # Saves massive memory when coordinates are sparse
    xs = sorted({x for x, _ in points})
    ys = sorted({y for _, y in points})

    # INTERLEAVED GRID: Create grid with size (2*n - 1) to fit both tiles AND spaces between them
    # Even indices (0, 2, 4, ...) = actual tile positions
    # Odd indices (1, 3, 5, ...) = space between tiles (for connecting green lines)
    # Example: 4 unique x-coords -> grid of width 7 (0,1,2,3,4,5,6)
    grid = [[0] * (len(ys) * 2 - 1) for _ in range(len(xs) * 2 - 1)]

    # DRAW POLYGON BOUNDARY: Connect consecutive red tiles with lines (red + green tiles)
    # zip(points, points[1:] + points[:1]) pairs each point with the next, wrapping last to first
    for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1]):
        # Convert original coordinates to compressed grid indices
        # xs.index(x1) finds position in sorted list, +2 converts to interleaved grid position
        cx1, cx2 = sorted([xs.index(x1) * 2, xs.index(x2) * 2])
        cy1, cy2 = sorted([ys.index(y1) * 2, ys.index(y2) * 2])

        # Fill rectangle between these two points (handles horizontal/vertical lines)
        # This marks both the red tiles and green connecting tiles as boundary (value = 1)
        for cx in range(cx1, cx2 + 1):
            for cy in range(cy1, cy2 + 1):
                grid[cx][cy] = 1

    # FLOOD FILL FROM OUTSIDE: Mark all cells reachable from outside the polygon
    # Start at (-1, -1) which is just outside the grid bounds
    outside = {(-1, -1)}
    queue = deque(outside)

    while len(queue) > 0:
        tx, ty = queue.popleft()

        # Check all 4 neighbors (up, down, left, right)
        for nx, ny in [(tx - 1, ty), (tx + 1, ty), (tx, ty - 1), (tx, ty + 1)]:
            # Skip if too far out of bounds (more than 1 step outside grid)
            if nx < -1 or ny < -1 or nx > len(grid) or ny > len(grid[0]):
                continue

            # Skip if it's a boundary cell (value = 1, meaning red and green tiles)
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                continue

            # Skip if already visited
            if (nx, ny) in outside:
                continue

            # Mark as outside and add to queue for continued flood fill
            outside.add((nx, ny))
            queue.append((nx, ny))

    # FILL INTERIOR: Any cell not reached by flood fill must be inside the polygon
    # Mark these interior cells as valid (green) by setting them to 1
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) not in outside:
                grid[x][y] = 1

    # BUILD PREFIX SUM ARRAY (PSA): Enables O(1) rectangle sum queries
    # psa[x][y] = sum of all grid values in rectangle from (0, 0) to (x, y)
    psa = [[0] * len(row) for row in grid]
    for x in range(len(psa)):
        for y in range(len(psa[0])):
            # Use inclusion-exclusion principles to compute prefix sum
            left = psa[x - 1][y] if x > 0 else 0    # Sum to the left
            top = psa[x][y - 1] if y > 0 else 0     # Sum above
            # Diagonal (counted twice, subtract once)
            topleft = psa[x - 1][y - 1] if x > 0 < y else 0
            psa[x][y] = left + top - topleft + grid[x][y]

    def valid(x1, y1, x2, y2):
        """
        Check if rectangle with corners at (x1, y1) and (x2, y2) contains ONLY valid tiles. 
        Uses prefix sum array for O(1) rectangle sum query.
        Returns True if all cells in rectangle are marked as valid (value = 1).
        """
        # Convert original coordinates to compressed grid indices
        cx1, cx2 = sorted([xs.index(x1) * 2, xs.index(x2) * 2])
        cy1, cy2 = sorted([ys.index(y1) * 2, ys.index(y2) * 2])

        # Calculate sum in rectangle using PSA with inclusion-exclusion principle
        # Sum(rect) = psa[bottom-right] - psa[left-column] - psa[top-row] + psa[top-left-corner]
        left = psa[cx1 - 1][cy2] if cx1 > 0 else 0
        top = psa[cx2][cy1 - 1] if cy1 > 0 else 0
        topleft = psa[cx1 - 1][cy1 - 1] if cx1 > 0 < cy1 else 0
        count = psa[cx2][cy2] - left - top + topleft

        # Rectangle is valid if ALL cells are marked (count equals total cells)
        return count == (cx2 - cx1 + 1) * (cy2 - cy1 + 1)

    # FIND LARGEST VALID RECTANGLE: Check all pairs of red tiles as potential corners
    # Calculate area in ORIGINAL coordinates (not compressed grid coordinates)
    # Only consider rectangles that are fully inside the polygon (valid returns True)
    max_rectangle = (max(
        # Area in original coordinate space
        (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        for i, (x1, y1) in enumerate(points)    # For each red tile
        # Pair with all previous tiles (avoid duplicates)
        for x2, y2 in points[:i]
        if valid(x1, y1, x2, y2)
    ))

    return max_rectangle


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to input file")
    args = parser.parse_args()
    input_path = args.input

    part_1_res = movie_theater_part1(input_path)
    print("Part 1: ", part_1_res)

    # part_2_res = movie_theater_part2(input_path)
    # print("Part 2: ", part_2_res)

    part_2_res = movie_theater_part2_opt(input_path)
    print("Part 2: ", part_2_res)


if __name__ == "__main__":
    main()
