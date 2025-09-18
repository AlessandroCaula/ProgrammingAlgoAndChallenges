################################
## Trace the Path of the Word ##
################################
# 18-09-2025

# Given a grid of letters, check if a word can be traced by moving up, down, left, or right from one letter to the next. 
# 
# Write a function that returns the path as a list of [row, col] positions, or "Not present" if the word is not found/can't be created.
# 
# EXAMPLE
#
# trace_word_path("BISCUIT", [
#   ["B", "I", "T", "R"],
#   ["I", "U", "A", "S"],
#   ["S", "C", "V", "W"],
#   ["D", "O", "N", "E"]
# ])
# output = [[0, 0], [1, 0], [2, 0], [2, 1], [1, 1], [0, 1], [0, 2]]

# trace_word_path("HELPFUL", [
#   ["L","I","T","R"],
#   ["U","U","A","S"],
#   ["L","U","P","O"],

def trace_word_path(word: str, grid: list[list[int]]):
    # Number of rows and cols
    rows, cols = len(grid), len(grid[0])

    # Recursive DFS function to search for the word
    def search(r, c, idx, path, visited):
        # 1. Check boundaries (must be inside grid)
        if not (0 <= r < rows and 0 <= c < cols):
            return False
        
        # 2. Avoid revisiting same cell in this path
        if (r, c) in visited:
            return False
        
        # 3. Current cell must match current character of word
        if grid[r][c] != word[idx]:
            return False
        
        # If we reach here, this cell is valid. Include it in path
        path.append([r, c])
        visited.add((r, c))

        # 4. Base case: if last character matched. Word is found
        if idx == len(word) - 1:
            return True
        
        # 5. Explore neighbors (down, up, right, left)
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            if search(r + dr, c + dc, idx + 1, path, visited):
                return True

        # 6. Backtrack if no neighbor works. Remove from path/visited
        path.pop()
        visited.remove((r, c))
        return False

    # Try to start search from every cell in the grid
    for r in range(rows):
        for c in range(cols):
            path = []
            visited = set()
            if search(r, c, 0, path, visited): # Start DFS if first letter matches
                return path

    # If no path forms the word, return "Not present"
    return "Not present"


word = "BISCUIT"
grid = [
    ["B", "I", "T", "R"],
    ["I", "U", "A", "S"],
    ["S", "C", "V", "W"],
    ["D", "O", "N", "E"]
]

print(trace_word_path(word, grid))