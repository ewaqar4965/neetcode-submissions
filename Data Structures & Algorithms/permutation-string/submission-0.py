class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #corner case
        if len(s1) > len(s2):
            return False
        
        freqS1 = {}
        freqS2 = {}
        for i in range(len(s1)):
            freqS1[s1[i]] = freqS1.get(s1[i], 0) + 1
        
        #sliding window to check:
        start = 0

        for end in range(len(s2)):
            freqS2[s2[end]] = freqS2.get(s2[end], 0) + 1

            #window is getting too big
            if ((end - start + 1) > len(s1)):
                freqS2[s2[start]] -= 1

                if freqS2[s2[start]] == 0:
                    del freqS2[s2[start]]

                start += 1
            
            if freqS1 == freqS2:
                return True
        
        return False

                

        





        
        