def isValid(s):
        if len(s) == 1:
            print(False)
        
        a = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                a.append(i)
            else:
                if len(a) == 0:
                     print(False)
                ch = a.pop()
                if (i == ")" and ch == "(") or (i == "}" and ch == "{") or (i == "]" and ch == "["):
                    continue
                else:
                     print(False)
        print( len(a) == 0)
    
s = "((({{[]}})})"
isValid(s)