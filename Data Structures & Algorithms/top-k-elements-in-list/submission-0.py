from collections import Counter
'''4 4 4 2 2 2 3 3 7777
7:4
4:3
2:3
3:2'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        num_freq= list(sorted(freq, key=lambda num: freq[num],reverse=True))
        sort_slice=num_freq[:k]
        return sort_slice



        