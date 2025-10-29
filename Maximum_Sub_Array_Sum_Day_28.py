def maxSum(arr):
    #get the length of array
    n = len(arr)
    total = 0
    #initialize maxium sum -infinity at the start
    maxi = float("-inf")
    for i in range(0, n):
        #add the every element to total so we can get the maximum sum
        total = total + arr[i]
        #now store the maximum sum in variable
        maxi = max(maxi, total)
        #if the value of total is negative then it will not help in get the maximum so make it zero
        if total < 0:
            total = 0
    
    print(f"Maximum subarray sum is : {maxi}")


arr = [-2, -1, 4, 5, -2, 5, 8, 9, 4, -1]
maxSum(arr)