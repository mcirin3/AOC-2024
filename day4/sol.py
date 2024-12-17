def count_xmas_occurrences(grid, word="XMAS"):
    # Dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])
    
    # Directions: (row step, col step)
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Down-right diagonal
        (1, -1),  # Down-left diagonal
        (-1, 1),  # Up-right diagonal
        (-1, -1)  # Up-left diagonal
    ]
    
    word_length = len(word)
    count = 0
    
    # Helper function to check if the word exists starting from (r, c) in a given direction
    def check_direction(r, c, dr, dc):
        for i in range(word_length):
            nr, nc = r + i * dr, c + i * dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i]:
                return False
        return True

    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Check in all 8 directions
            for dr, dc in directions:
                if check_direction(r, c, dr, dc):
                    count += 1

    return count
def count_xmas_patterns(file_path):
    # Read grid from the input file
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file]

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Helper function to check if a diagonal contains M, A, S
    def is_valid_diagonal(row, col):
        try:
            # Check diagonals around the cell (row, col)
            return ({grid[row - 1][col - 1], grid[row + 1][col + 1]} == {"M", "S"} and
                    {grid[row - 1][col + 1], grid[row + 1][col - 1]} == {"M", "S"})
        except IndexError:
            return False

    # Traverse through each cell in the grid while avoiding the edges
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] == "A":
                if is_valid_diagonal(r, c):
                    count += 1

    return count
# Read the grid from input.txt
with open("input.txt", "r") as file:
    grid = [line.strip() for line in file]
# Count occurrences of XMAS
result = count_xmas_occurrences(grid)
result2 = count_xmas_patterns("input.txt")
print("Total occurrences of XMAS:", result)
print("Total of XMAS patterns: ", result2)
