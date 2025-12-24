import sys
sys.stdout.reconfigure(encoding='utf-8')




def issafe(row, col, board, n):
    print(f"  Checking safety for position (row={row}, col={col})")

    duprow = row
    dupcol = col

    # Top-left diagonal
    while row >= 0 and col >= 0:
        if board[row][col] == "Q":
            print(f"    ❌ Queen found at top-left diagonal ({row},{col})")
            return False
        row -= 1
        col -= 1

    row = duprow
    col = dupcol

    # Same row (left side)
    while col >= 0:
        if board[row][col] == "Q":
            print(f"    ❌ Queen found in same row at ({row},{col})")
            return False
        col -= 1

    row = duprow
    col = dupcol

    # Bottom-left diagonal
    while row < n and col >= 0:
        if board[row][col] == "Q":
            print(f"    ❌ Queen found at bottom-left diagonal ({row},{col})")
            return False
        row += 1
        col -= 1

    print(f"    ✅ Position (row={row}, col={col}) is SAFE")
    return True


def solve(n, board, col, ans):
    print(f"\n➡️  Entering column {col}")

    # Base case: all columns filled
    if col == n:
        print("🎉 Solution found:")
        for r in board:
            print("   ", r)
        print()
        ans.append(list(board))
        return

    # Try every row in this column
    for row in range(n):
        print(f"\nTrying row {row} in column {col}")

        if issafe(row, col, board, n):

            # Place queen
            print(f"  ➕ Placing Q at ({row},{col})")
            board[row] = board[row][:col] + "Q" + board[row][col+1:]

            print("  Board after placing:")
            for r in board:
                print("   ", r)

            # Recurse to next column
            solve(n, board, col + 1, ans)

            # Backtrack
            print(f"  🔄 Backtracking from ({row},{col})")
            board[row] = board[row][:col] + "." + board[row][col+1:]

            print("  Board after backtracking:")
            for r in board:
                print("   ", r)
        else:
            print(f"  ❌ Cannot place Q at ({row},{col})")

            
n = 4

board = ["." * n for _ in range(n)]
ans = []

print("🚀 Starting N-Queens Solver\n")
solve(n, board, 0, ans)

print("\n✅ All solutions:")
print(len(ans))
