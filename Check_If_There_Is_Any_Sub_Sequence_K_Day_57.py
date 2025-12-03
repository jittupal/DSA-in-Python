def solved(index, subset, arr, result, k, total):
    if total == k:
        result.append(subset.copy())
        return True
    elif total > k:
        return False
    
    if index >= len(arr):
        return False
    
    subset.append(arr[index])
    sums = total + arr[index]
    pick = solved(index + 1, subset, arr, result, k, sums)
    if pick == True:
        return True
    subset.pop()
    sums = total
    not_pick = solved(index + 1, subset, arr, result, k, sums)
    return not_pick
    

arr = [1, 2, 3, 3]
subest = []
result = []
index = 0
k = 9
total = 0

print("There is exist the solution: " , solved(index, subest, arr, result, k, total))