from collections import deque

def find_start_end(maze):
    start = None
    end = None
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)
    return start, end

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

def is_valid(r, c, rows, cols, maze, visited):
    return (0 <= r < rows and
            0 <= c < cols and
            maze[r][c] != '#' and
            (r, c) not in visited)

def bfs(maze):
    start, end = find_start_end(maze)
    if not start or not end:
        return None  # start or end not found
    
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == end:
            return path
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc, rows, cols, maze, visited):
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
    return None  # no path found

def dfs(maze):
    start, end = find_start_end(maze)
    if not start or not end:
        return None
    
    rows, cols = len(maze), len(maze[0])
    stack = [(start, [start])]
    visited = set([start])

    while stack:
        (r, c), path = stack.pop()
        if (r, c) == end:
            return path
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc, rows, cols, maze, visited):
                visited.add((nr, nc))
                stack.append(((nr, nc), path + [(nr, nc)]))
    return None

def print_path(maze, path):
    maze_copy = [list(row) for row in maze]
    for r, c in path:
        if maze_copy[r][c] not in ('S', 'E'):
            maze_copy[r][c] = '*'
    for row in maze_copy:
        print(''.join(row))

# Example usage:
maze = [
    "#########",
    "#S #    #",
    "#  # ## #",
    "# ## #  #",
    "#    ##E#",
    "#########"
]

print("BFS shortest path:")
path_bfs = bfs(maze)
if path_bfs:
    print_path(maze, path_bfs)
else:
    print("No path found")

print("\nDFS any path:")
path_dfs = dfs(maze)
if path_dfs:
    print_path(maze, path_dfs)
else:
    print("No path found")

