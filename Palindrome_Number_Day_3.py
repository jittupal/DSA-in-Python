# You have a ineger n and you have to check if this is palindrome or not.
#Palindorme is a word which is same from left to right or right to left like 121, NITIN, 1001

def Palindrome(n):
    num = n
    result = 0
    while num > 0:
        last = num % 10
        result = (result * 10) + last
        num = num // 10

    return result

a = int(input("Enter a number "))
answer = Palindrome(a)

if (a == answer ):
    print("palindrome")
else:
    print("not a palindrome")