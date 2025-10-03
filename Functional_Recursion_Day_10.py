# Function to calculate the sum of first n natural numbers using recursion
def sumNa(n):
    # Base case: if n is 1, just return 1
    if n == 1:
        return 1
    # Recursive case: add current n to the sum of (n-1)
    return n + sumNa(n-1)

n = 10
sum = sumNa(n)
# This will eventually compute 10 + 9 + 8 + ... + 1
print(f"sum of first {n} natural numbers is : {sum}")


# Function to calculate the sum of elements in a list using recursion
def listsum(list1):
    # Base case: if list has only one element, return that element
    if len(list1) == 1:
        return list1[0]
    # Recursive case: take the first element and add it to the sum of the rest of the list
    return list1[0] + listsum(list1[1:])

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = listsum(list1)
# This will eventually compute 1 + 2 + 3 + ... + 10
print(f"sum of list numbers is : {sum}")

#Function to calculate Factorial of number using recursion 
def fact(n):
    #Base Case: if the number is 1 then return 1
    if n == 1:
        return 1
    #Recursive Case: take the number and multiply it by rest of the numbers
    return n * fact(n-1)

n = 6
ans = fact(n)
#The flow will goes like 6 * 5 * 4 * ... * 1
print(f"factorial of {n} is : {ans}")