arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 4
sums = 20
ans = 0
b = False
for i in range(0, k):
    ans += arr[i]
    
for i in range(k, len(arr)):
    ans += arr[i]
    ans -= arr[i-k]
    
    if ans == sums:
        b = True
    
print(b)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 4
sums = 10
ans = []
b = False
for i in range(0, k):
    ans.append(arr[i])
    
for i in range(k, len(arr)):
    if sum(ans) == sums:
        b = True
        break
    
    ans.pop(0)
    ans.append(arr[i])
    
if b:
    print(ans)
else:
    print(b)