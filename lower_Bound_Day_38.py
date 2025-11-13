def lowerBound(arr, target):
    lb = len(arr)
    l = 0
    h = len(arr) -1

#run the loop until the all the h and l overlap
    while l <= h:
        mid = (l + h) // 2
        #if value of mid is grater or equal to target then it might be smallest but there will be possible of more lower index
        if arr[mid] >= target:
            lb = mid
            h = mid -1
        elif arr[mid] < target:
            l = mid + 1
        else:
            h = mid - 1
    print(f"The lower bound is at index {lb}")


arr = [1, 1, 1, 2, 2, 3, 3, 3, 6, 7, 8, 9]
lowerBound(arr, 9)