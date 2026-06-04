class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checkDup = set()
        start = 0
        maxLength = 0

        for end in range(len(s)):
            while s[end] in checkDup:
                checkDup.discard(s[start])
                start += 1

            checkDup.add(s[end])
            maxLength = max(maxLength, end - start + 1)
        
        return maxLength
            

        