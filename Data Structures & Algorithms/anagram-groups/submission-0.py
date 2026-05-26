class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a default dict
        res = defaultdict(list)

        for i in strs:
            count = [0] * 26

            for j in i:
                #deal with indexing
                count[ord(j) - ord('a')] += 1
            
            #add to hashmap
            res[tuple(count)].append(i)

        return list(res.values())
