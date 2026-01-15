def PrefixToInfix(s):
    stack = []
    s = s[::-1]
    
    for char in s:
        if char.isalnum():
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            new_expression = f"({operand2}{char}{operand1})"
            
            # new_expression = new_expression[::-1]
            
            stack.append(new_expression)
            
    return stack[-1]


s = "*+AB-CD"

ans = PrefixToInfix(s)

print(ans)