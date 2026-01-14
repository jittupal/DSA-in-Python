def PostfixToInfix(s):
    stack = []
    
    for char in s:
        if char.isalnum():
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            new_expression = f"({operand1}{char}{operand2})"
            
            stack.append(new_expression)
            
    return stack[-1]
    
s = "AB-DE+F*/"

ans = PostfixToInfix(s)

print(ans)