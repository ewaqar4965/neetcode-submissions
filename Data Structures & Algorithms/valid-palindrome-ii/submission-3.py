class Solution:
    def validPalindrome(self, s: str) -> bool:
        #define pointers
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                #determine which substr is valid
                skipL = s[left + 1: right + 1]
                skipR = s[left: right]

                return skipL == skipL[::-1] or skipR == skipR[::-1]
            
            left += 1
            right -= 1
        
        return True