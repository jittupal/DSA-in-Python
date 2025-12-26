def solve(maze, ans, n, visited, direction, row, col):
    if col == n - 1 and row == n - 1:
        ans.append(direction)
        return
    
    #down
    if row + 1 < n and not visited[row + 1][col] and maze[row+1][col] == 1:
        visited[row][col] = 1
        solve(maze, ans, n, visited, direction + "D", row + 1, col)
        visited[row][col] = 0
    
    #left
    if col - 1 >= 0 and not visited[row][col - 1] and maze[row][col - 1] == 1:
        visited[row][col] = 1
        solve(maze, ans, n, visited, direction + "L", row, col-1)
        visited[row][col] = 0
    
    #right
    if col + 1 < n and not visited[row][col + 1] and maze[row][col + 1] == 1:
        visited[row][col] = 1
        solve(maze, ans, n, visited, direction + "R", row, col + 1)
        visited[row][col] = 0
    
    #up
    if row - 1 >= 0 and not visited[row - 1][col] and maze[row - 1][col] == 1:
        visited[row][col] = 1
        solve(maze, ans, n, visited, direction + "U", row - 1, col)
        visited[row][col] = 0
    




maze = [[1,0,0,0], [1,1,0,1], [1,1,0,0], [0,1,1,1]]
n = len(maze)
visited = [[0] * n for _ in range(n)]
ans = []
row = 0
col = 0
direction = ""

solve(maze, ans, n, visited, direction, row, col)
print(ans)