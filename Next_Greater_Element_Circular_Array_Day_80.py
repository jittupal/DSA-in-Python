def nextgreater(arr):
    n = len(arr)
    ans = [-1] * n
    stack = []
    
    for i in range(2*n-1, -1, -1):
        while len(stack) != 0 and stack[-1] <= arr[i%n]:
            stack.pop()
        
        if i < n:
            if len(stack) != 0:
                ans[i] = stack[-1]
                
        stack.append(arr[i%n])
        
    return ans

arr = [12, 1, 4, 9, 11, 5]

ans = nextgreater(arr)

print(ans)