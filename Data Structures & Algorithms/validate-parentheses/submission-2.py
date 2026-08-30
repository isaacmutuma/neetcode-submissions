class Solution:
    def isValid(self, s: str) -> bool:
        par={
            '(' : ')',
            '{' : '}',
            '[' : ']',
        }
        stack=[]
        for char in s:
            if char in par.keys():
                stack.append(char)
            else:
                if not stack or char!= par[stack[-1]]:
                    return False
                stack.pop()
        return not stack