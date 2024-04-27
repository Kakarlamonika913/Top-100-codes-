def is_balanced(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                return False
    return not stack
print(is_balanced("()"))      
print(is_balanced("()[]{}"))   
print(is_balanced("(]"))      
print(is_balanced("([)]"))     
