"""results={
    "act":['Cat','act']
    "opts":["stop", "pots", "tops"]
    "aht":["hat"]
}"""

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       results=defaultdict(list) 
       for word in strs:
        key="".join(sorted(word))
        results[key].append(word)
       output=list(results.values())
       return output

