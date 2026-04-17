class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for i in range(0, len(nums)):
            if nums[i] in hashSet:
                return True
            else:
                hashSet.add(nums[i])

        return False

        