class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]

        def backtrack(current="",open=0,close=0):
            if open==n and close==n:
                result.append(current)
                return
            if open<n:
                backtrack(current +"(",open+1,close)
            if close<open:
                backtrack(current +")",open,close+1)

        backtrack()
        return result


