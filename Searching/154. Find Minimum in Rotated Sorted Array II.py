class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                # Minimum must be in right half
                left = mid + 1
            elif nums[mid] < nums[right]:
                # Minimum is in left half (including mid)
                right = mid
            else:
                # nums[mid] == nums[right], can't decide, shrink right
                right -= 1
        
        return nums[left]
nums = [2,2,2,0,1]
print(Solution().findMin(nums))  # Output: 0
