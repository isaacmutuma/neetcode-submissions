class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[] # to keep track of days waiting for a better reading
        for day in range(len(temperatures)):
            while stack and temperatures[day] > temperatures[stack[-1]]:
                waiting_day=stack.pop()
                result[waiting_day]= day-waiting_day
            stack.append(day)
        return result
            

        
        