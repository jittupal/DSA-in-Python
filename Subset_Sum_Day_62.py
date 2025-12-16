def solve( index, arr, total, result):
    if index >= len(arr):
        result.append(total)
        return
    
    sums = total + arr[index]
    solve(index+1, arr, sums, result)
    sums = total
    solve(index + 1, arr, sums, result)
    
arr =  [ 1, 2, 3]
index = 0
total = 0
result = []
solve(index, arr, total, result)
print(result)

    