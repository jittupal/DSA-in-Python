def solve(board, col, n, ans, leftrow, upperdiagonal, lowerdiagonal):
    if col == n:
        ans.append(list(board))
        return
    
    for row in range(n):
        if (
            leftrow[row] == 0
            and upperdiagonal[row + col] == 0
            and lowerdiagonal[n-1 + col - row] == 0
        ):
            board[row] = board[row][:col] + "Q" + board[row][col+1:]
            leftrow[row] = 1
            upperdiagonal[row + col] = 1
            lowerdiagonal[n - 1 + col - row] = 1
            
            solve(board, col+1, n, ans, leftrow, upperdiagonal, lowerdiagonal)
            
            board[row] = board[row][:col] + "." + board[row][col+1:]
            leftrow[row] = 0
            upperdiagonal[row + col] = 0
            lowerdiagonal[n - 1 + col - row] = 0
        
n = 4
board = ["." * n for _ in range(n)]
ans = []
leftrow = [0] * n
upperdiagonal = [0] * (2 * n - 1)
lowerdiagonal = [0] * (2 * n - 1)
solve(board, 0, n, ans, leftrow, upperdiagonal, lowerdiagonal)
print(ans)