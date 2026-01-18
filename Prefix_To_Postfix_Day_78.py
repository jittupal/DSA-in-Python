def PrefixToPostfix(s):
    stack = []
    s = s[::-1]
    
    for char in s:
        if char.isalnum():
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            new_expression = operand2 + operand1 + char
            
            stack.append(new_expression)
            
    return stack[-1]

s = "*+AB-CD"

ans = PrefixToPostfix(s)
print(ans)