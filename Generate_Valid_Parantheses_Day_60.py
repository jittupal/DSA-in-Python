
def solve( index, brackets, result, total, n):
        if index >= n:
            if total == 0:
                result.append("".join(brackets))
            return
        if total > n//2 or total < 0:
                return

        brackets[index] = "("
        sums = total + 1
        solve(index+1, brackets, result, sums, n)
        brackets[index] = ")"
        sums = total - 1
        solve(index+1, brackets, result, sums, n)
        

n = 10
brackets = [""] * n
result = []
total = 0
index = 0
solve(index, brackets, result, total, n)
print(result)