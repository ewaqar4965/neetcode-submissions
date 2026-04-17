class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #ensure they are the same size
        if len(s) != len(t):
            return False
        
        #they are the same size, create hashmaps
        countS, countT = {}, {}

        for i in range (len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT