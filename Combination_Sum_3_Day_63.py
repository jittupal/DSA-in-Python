def solve(k, n, result, total, subset, index):
    if len(subset) == k:
        if total == n:
            result.append(subset.copy())
        return
    if total > n:
        return
    if index >= 10:
        return
    
    subset.append(index)
    sums = total + index
    solve(k, n, result, sums, subset, index+1)
    subset.pop()
    sums = total
    solve(k, n, result, sums, subset, index+1)
    
index = 1
total = 0
subset = []
result = []
n = 15
k = 4
solve(k, n, result, total, subset, index)
print(result)