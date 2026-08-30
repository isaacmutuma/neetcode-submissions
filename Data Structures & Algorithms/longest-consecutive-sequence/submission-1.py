class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        track=0
        nums_arr=set(nums)
        for num in  nums_arr:
            if num-1 not in nums_arr:
                length=1
                starter=num
                while starter+1 in nums_arr:
                    starter=starter+1
                    length+=1
                if length>track:
                    track=length
        return track       


                

           
        




        