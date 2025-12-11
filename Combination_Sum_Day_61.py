def solve(arr, target, subset, total, index, result):
    if total == target:
        result.append(subset.copy())
        return
    elif total > target:
        return
    
    if index >= len(arr):
        return
    
    sums = total + arr[index]
    subset.append(arr[index])
    solve(arr, target, subset, sums, index, result)
    sums = total
    subset.pop()
    solve(arr, target, subset, sums, index+1, result)
    

arr = [1, 2, 3]
target = 4
result = []
subset = []
index = 0
total = 0

solve(arr, target, subset, total, index, result)

print(result)