#function to calculate fibonacci using recursin
def func(n):
    if n == 0 or n == 1:
        return n
    return func(n-1) + func(n-2)

n = 7
ans = func(n)
print(f"answer of {n}th fibonacci number is : {ans}")

#function to check if string is palindrome or not
def func(s, i, j):
    if i >= j:
        return True
    if s[i] != s[j]:
        return False
    return func(s, i+1, j-1)

s = "mam"
ans = func(s, 0, len(s) - 1)
if ans == True:
    print(f"{s} is palindorme")
else:
    print(f"{s} is not palindorme")