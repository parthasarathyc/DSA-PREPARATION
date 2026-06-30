from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                # Peak is on the left side (including mid)
                right = mid
            else:
                # Peak is on the right side
                left = mid + 1
        
        return left
nums = [1,2,3,1]
print(Solution().findPeakElement(nums))  # Output: 2 (nums[2] = 3)
