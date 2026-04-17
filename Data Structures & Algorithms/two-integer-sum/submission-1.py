class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create an unordered map
        numsMap = {}

        #populate the map
        for i, n in enumerate(nums):
            compliment = target - n

            if compliment in numsMap:
                return [numsMap[compliment], i]

            numsMap[n] = i