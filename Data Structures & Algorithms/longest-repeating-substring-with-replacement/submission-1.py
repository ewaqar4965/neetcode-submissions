class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxLength = 0
        maxFreq = 0
        start = 0
        

        for end in range(len(s)):
            freq[s[end]] = freq.get(s[end], 0) + 1
            maxFreq = max(maxFreq, freq[s[end]])

            while ((end - start + 1) - maxFreq) > k:
                freq[s[start]] -= 1

                if freq[s[start]] == 0:
                    del freq[s[start]]
                
                start += 1

            maxLength = max(maxLength, end - start + 1)
        
        return maxLength


    

        