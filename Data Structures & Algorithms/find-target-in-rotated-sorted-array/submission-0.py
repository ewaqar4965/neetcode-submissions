class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while(left <= right):
            midpoint = (left + right) // 2

            if target == nums[midpoint]:
                return midpoint

            #left side is sorted
            if nums[left] <= nums[midpoint]:
                if nums[left] <= target < nums[midpoint]:
                    right = midpoint - 1
                
                else:
                    left = midpoint + 1
                
            #right side is sorted
            else:
                if nums[midpoint] < target <= nums[right]:
                    left = midpoint + 1
                else:
                    right = midpoint - 1
        
        return -1


        