def isValid(string):
    bracketMapping = {"(":")", "[":"]", "{":"}"}
    openParams = set(["(","[","{"])
    stack = []
    for s in string:
        if s in openParams:   
            stack.append(s)
        elif stack and s==bracketMapping[stack[-1]]:
             stack.pop()
        else:
            return False
    return stack == []
string  = "{[()]}}"
if  isValid(string):
    print("Valid Parenthesis")
    
else:
    print("invalid parenthesis")

