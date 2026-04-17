class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #make a freq hash map
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        #check if it exists for the other arr
        for j in t:
            if j in freq:
                freq[j] -= 1
                if freq[j] == 0:
                    del freq[j]
            else:
                return False

        if len(freq) != 0:
            return False
        
        return True