class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                print(stack)
                if not stack:
                    return False
                if i == ')' and stack[-1] != '(':
                    return False
                if i == ']' and stack[-1] != '[':
                    return False
                if i == '}' and stack[-1] != '{':
                    return False
                stack.pop()
        return not stack
    
# Test the function
s = "()"
print(Solution().isValid(s))  # Output: True
s = "([{}])"
print(Solution().isValid(s))  # Output: True