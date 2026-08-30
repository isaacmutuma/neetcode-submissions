class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[]# stores the day indices
        for day in range(len(temperatures)):
            while stack and temperatures[day] > temperatures[stack[-1]]:
                idx=stack.pop() # day waiting for the warmer one to come
                result[idx]=day-idx # how long did idx wait till day arrived
            stack.append(day)       
        return result

           

        