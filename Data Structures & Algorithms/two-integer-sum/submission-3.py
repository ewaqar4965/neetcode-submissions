class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}
        
        for i in range(len(nums)):
            need = target - nums[i]

            if need in indexMap:
                return [indexMap[need], i]
            
            indexMap[nums[i]] = i

        return
        