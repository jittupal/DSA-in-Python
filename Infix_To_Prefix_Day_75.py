class Solution:
    def Precedence(self, ch):
        if ch == '+' or ch == '-':
            return 1
        if ch == '*' or ch == '/':
            return 2
        if ch == '^':
            return 3
        return 0
    
    def infixToPrefix(self, s):
        s = s[::-1]
        s = s.replace("(", "temp").replace(")", "(").replace("temp", ")")
        stack = []
        result = []
        
        for char in s:
            if ("a" <= char <= "z") or ("A" <= char <= "Z") or ("0" <= char <= "9"):
                result.append(char)
            elif char == "(":
                stack.append(char)
            elif char == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop()
            else:
                while (
                    stack and
                    (
                        self.Precedence(stack[-1]) > self.Precedence(char) or
                        (
                            self.Precedence(stack[-1]) == self.Precedence(char)
                            and char == '^'
                        )
                    )
                ):
                    result.append(stack.pop())
                stack.append(char)
            
        while stack:
            result.append(stack.pop())
        
        return "".join(result[::-1])


S = Solution()
print(S.infixToPrefix("a*b+c/d+"))