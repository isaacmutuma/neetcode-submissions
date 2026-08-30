class Solution:
    def isPalindrome(self, s: str) -> bool:
        strip= ("".join(filter(str.isalnum,s))).lower()
        reverse = (strip[::-1])
        return strip == reverse

        