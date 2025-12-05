def solved(index, arr,  k, total):
    if total == k:
        return 1
    elif total > k:
        return 0
    
    if index >= len(arr):
        return 0
    
    sums = total + arr[index]
    pick = solved(index + 1, arr, k, sums)
    sums = total
    not_pick = solved(index + 1, arr, k, sums)
    return not_pick + pick
    

arr = [1, 2, 3, 3]
subest = []
result = []
index = 0
k = 3
total = 0

print("There is exist the solution: " , solved(index, arr, k, total))