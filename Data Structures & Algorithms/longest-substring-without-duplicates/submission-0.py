class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #create a set
        numSet = set()
        maxLen = 0
        start = 0
        
        for end in range(len(s)):
            #if its a duplicate keep moving the start pointer
            while s[end] in numSet:
                numSet.remove(s[start])
                start += 1
            
            numSet.add(s[end])
            maxLen = max(maxLen, end - start + 1)
        
        return maxLen



        