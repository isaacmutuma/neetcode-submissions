class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators=['+','-', '*','/']
        stack=[]
        for token in tokens:
            if token not in operators:
                 stack.append(int(token))
            else:
                 if token == '+':
                    b=stack.pop()
                    a=stack.pop() 
                    result = a + b
                 elif token == '-':
                    b=stack.pop()
                    a=stack.pop() 
                    result = a - b
                 elif token == '*':
                    b=stack.pop()
                    a=stack.pop() 
                    result = a * b
                 else:
                    b=stack.pop()
                    a=stack.pop() 
                    result = int(a / b)
                 stack.append(result)
        return stack[-1]

            