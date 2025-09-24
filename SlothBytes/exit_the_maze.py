#############################
## Can you Exit the Maze ? ##
#############################
# 24-09-2025

# You are given a 2D matrix representing a maze, where 0 is a walkable path and 1 is a wall
# 
# You start at the top-left corner and you have to reach the bottom-right corner.
# 
# Write a function that returns True if a path exists.
# 
# You can only move up, down, left and right. You cannot move diagonally
# 
# EXAMPLE
# 
# canExit([
#   [0, 1, 1, 1, 1, 1, 1],
#   [0, 0, 1, 1, 0, 1, 1],
#   [1, 0, 0, 0, 0, 1, 1],
#   [1, 1, 1, 1, 0, 0, 1],
#   [1, 1, 1, 1, 1, 0, 0]
# ])
# output = True

# canExit([
#   [0, 1, 1, 1, 1, 1, 1],
#   [0, 0, 1, 0, 0, 1, 1],
#   [1, 0, 0, 0, 0, 1, 1],
#   [1, 1, 0, 1, 0, 0, 1],
#   [1, 1, 0, 0, 1, 1, 1]
# ])
# output = False
# # This maze only has dead ends!

# canExit([
#   [0, 1, 1, 1, 1, 0, 0],
#   [0, 0, 0, 0, 1, 0, 0],
#   [1, 1, 1, 0, 0, 0, 0],
#   [1, 1, 1, 1, 1, 1, 0],
#   [1, 1, 1, 1, 1, 1, 1]
# ]) 
# output = False

# # Exit only one block away, but unreachable!

# canExit([
#   [0, 1, 1, 1, 1, 0, 0],
#   [0, 0, 0, 0, 1, 0, 0],
#   [1, 1, 1, 0, 0, 0, 0],
#   [1, 0, 0, 0, 1, 1, 0],
#   [1, 1, 1, 1, 1, 1, 0]
# ])
# output = True

def can_exit(maze: list[list[int]]) -> bool:
    maze_last_row = len(maze) - 1
    maze_last_col = len(maze[maze_last_row]) - 1

    start_point = (0, 0)
    end_point = (maze_last_row, maze_last_col)

    # Initialize the queue and the visited cell
    queue = [start_point]
    visited = [start_point]

    # Loop until the queue is empty
    while len(queue) > 0:
        # pop the element in the queue and search the neighbors for available cells
        (curr_r, curr_c) = queue.pop()
        # Check the neighbors cells
        for r, c in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            # Compute the new neighbor cell
            n_r = curr_r + r
            n_c = curr_c + c

            # Check if this neighbor is a valid one, does not exit from the maze dimension
            if (n_r < 0 or n_r > maze_last_row) or (n_c < 0 or n_c > maze_last_col):
                continue

            # If the new neighbor cell is a wall ("1"), skip it
            if maze[n_r][n_c] == 1:
                continue

            # Otherwise, check if the new neighbor is the end_point. If it is, then the maze has a solution
            if n_r == end_point[0] and n_c == end_point[1]:
                return True

            # Otherwise, if the cell has not been visited yet, just add it to the queue and the visited nodes
            if (n_r, n_c) not in visited:
                visited.append((n_r, n_c))
                queue.append((n_r, n_c))

    # If we have visited all the possible available cells ("0") and we have not found the end/exit point, then the maze does not have solution
    return False


maze = [
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 1, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 0, 0]
]
print(can_exit(maze)) # True

maze = [
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 0, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 0, 1, 0, 0, 1],
  [1, 1, 0, 0, 1, 1, 1]
]
print(can_exit(maze)) # False

print(can_exit([
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1]
]))
# output = False

print(can_exit([
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 0, 0, 0, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 0]
]))
# output = True