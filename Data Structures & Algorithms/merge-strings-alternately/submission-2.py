class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        finalStr = ""

        p1 = 0
        p2 = 0

        while(p1 < len(word1) and p2 < len(word2)):
            finalStr += word1[p1]
            finalStr += word2[p2]

            p1 += 1
            p2 += 1
        
        
        finalStr += (word1[p1:])
        finalStr += (word2[p2:])
        
        
        return finalStr
        