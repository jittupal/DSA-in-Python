n = 5
k = 3



result = ""
while k > -1:
    print("k :", k)
    if n % 2 == 1:
        print("n : ", n)
        print("if condition")
        result += "1"
    else:
        print("n : ", n)
        result += "0"
    n = n // 2
    k -= 1
result = result[::-1]
print(result)
if result[0] == '1':
    print("True")
else:
    print("False")
    
    
n = 5
k = 3  
if ((n >> k) & 1) == 1:
    print("True")
else:
    print("False")
    
a = 10
i = 2
#set kth bit set
print(a | (1 << i))

#clear kth bit
b = 13
i = 2
an = ~(1 << i)

print(b & an)

#remove the last set bit
c = 40

print(c & c-1)

#check if number is power of 2
d = 16
ans = d & d-1
if ans == 0:
    print("Number is power of 2")
else:
    print("Number is not power of 2")