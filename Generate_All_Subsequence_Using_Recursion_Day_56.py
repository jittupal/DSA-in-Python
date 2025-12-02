def solve(index, subset, arr, result):
    if index >= len(arr):
        result.append(subset.copy())
        return
        
    
    subset.append(arr[index])
    solve(index + 1, subset, arr, result)
    subset.pop()
    solve(index + 1, subset, arr, result)
    

arr = [1, 2]
subest = []
result = []
index = 0

solve(index, subest, arr, result)
print(result)


def solved(index, subset, arr, result, k):
    if index >= len(arr):
        if sum(subset) == k:
            
             result.append(subset.copy())
        return
        
    
    subset.append(arr[index])
    solved(index + 1, subset, arr, result, k)
    subset.pop()
    solved(index + 1, subset, arr, result, k)
    

arr = [1, 2, 3, 9, 5, 4,]
subest = []
result = []
index = 0
k = 9

solved(index, subest, arr, result, k)
print(result)