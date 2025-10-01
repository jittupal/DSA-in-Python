n = 1221
num = n
result = 0

def palindrome(num, result):
    # Print current state of variables (for dry run)
    print(f"NUM : {num}, Result : {result}")
    
    # Base condition: if number is reduced to 0, return the result
    if num == 0:
        return result
    
    # Take the last digit of num
    last = num % 10
    
    # Build reversed number step by step
    result = (result * 10) + last
    
    # Remove last digit from num
    num = num // 10
    
    # Recursive call with smaller number
    return palindrome(num, result)


# Call the function
ans = palindrome(num, result)

# Final result after recursion finishes
print(f"result : {ans}")

# Check palindrome condition
if ans == n:
    print("palindrome")
else:
    print("Not Palindrome")