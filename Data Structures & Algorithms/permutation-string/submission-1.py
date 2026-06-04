class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Edge case
        if len(s1) > len(s2):
            return False

        #populate the first string
        freq1 = {}
        for i in range(len(s1)):
            freq1[s1[i]] = freq1.get(s1[i], 0) + 1
        
        start = 0
        freq2 = {}
        
        for end in range(len(s2)):
            freq2[s2[end]] = freq2.get(s2[end], 0) + 1

            while (end - start + 1) > len(s1):
                freq2[s2[start]] -= 1
                
                if freq2[s2[start]] == 0:
                    del freq2[s2[start]] 
                start += 1
            
            if freq1 == freq2:
                return True
        
        return False
            
        