def solve_maze(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False
        if maze[row][col] == '#':
            return False
        if visited[row][col]:
            return False
        if (row, col) == end:
            return True

        visited[row][col] = True

        if dfs(row - 1, col):  # Up
            return True
        if dfs(row + 1, col):  # Down
            return True
        if dfs(row, col - 1):  # Left
            return True
        if dfs(row, col + 1):  # Right
            return True

        return False

    return dfs(start[0], start[1])

# Example usage:
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', '#', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', 'E', '#', '#', '#', '#', '#'],
]
start = (1, 1)
end = (6, 6)

if solve_maze(maze, start, end):
    print("Maze solved!")
else:
    print("No solution found.")


"""
- Znajduje gdzie jest R
- Znajduje gdzie ma być wyjście
- bierze ich współrzędne
- i potem DFS
"""