class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        start = 0
        maxLen = 0
        maxFreq = 0

        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1
            maxFreq = max(maxFreq, count[s[end]])

            while((end - start + 1) - maxFreq > k):
                count[s[start]] -= 1
                start += 1

            maxLen = max(maxLen, end - start + 1)

        return maxLen
            

        