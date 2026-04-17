class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create a set
        numSet = set()
        
        for i in range(0, len(nums)):
            if nums[i] in numSet:
                return True
            
            numSet.add(nums[i])

        return False