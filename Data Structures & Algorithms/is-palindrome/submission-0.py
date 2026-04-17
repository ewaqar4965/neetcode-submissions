class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[right].isalnum() == False:
                right -= 1
                continue
            elif s[left].isalnum() == False:
                left += 1
                continue
            else:
                if s[right].lower() == s[left].lower():
                    left += 1
                    right -= 1
                else:
                    return False
        
        return True