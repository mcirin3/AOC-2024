from collections import deque

def parse_map_from_file(filename):
    """Reads the input map from a file and parses it into a 2D grid."""
    with open(filename, 'r') as file:
        return [list(map(int, line.strip())) for line in file.readlines()]
    
def find_trailheads(grid):
    trailheads = [] 
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                trailheads.append((r,c))
    return trailheads

def bfs_trail_score(grid, start):
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1), (1,0),(0,-1),(-1,0)]
    visited = set()
    queue = deque([start])
    reachable_nines = set()
    
    while queue:
        r, c = queue.popleft()
        if (r,c) in visited:
            continue
        visited.add((r,c))
        #if current position is 9 add to reachable nines
        
        if grid[r][c] == 9:
            reachable_nines.add((r,c))
            continue
        
        #explore neightbors with valid height incrememnt 
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if grid[nr][nc] == grid[r][c] + 1:
    
                    queue.append((nr, nc))
    return len(reachable_nines)

def dfs_count_paths(grid, r, c, visited):
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1), (1,0),(0,-1),(-1,0)]
     # If we reach a '9', this is a distinct trail
    if grid[r][c] == 9:
        return 1

    # Mark the current position as visited
    visited.add((r, c))
    count = 0

    # Explore neighbors
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
            if grid[nr][nc] == grid[r][c] + 1:  # Valid uphill step
                count += dfs_count_paths(grid, nr, nc, visited)

    # Backtrack: unmark the current position as visited
    visited.remove((r, c))
    return count
    


def calculate_total_score(filename):
    grid = parse_map_from_file(filename)
    trailheads = find_trailheads(grid)
    total_score = sum(bfs_trail_score(grid, trailhead) for trailhead in trailheads)
    
    return total_score
def calculate_total_ratings(filename):
    grid = parse_map_from_file(filename)
    trailheads = find_trailheads(grid)
    
    total_rating = 0
    for trailhead in trailheads:
        visited = set()
        total_rating += dfs_count_paths(grid, trailhead[0], trailhead[1], visited)
    return total_rating

input_file = "input.txt"
print(calculate_total_score(input_file), calculate_total_ratings(input_file))