from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Binary search boundaries
        left, right = max(nums), sum(nums)
        
        # Helper: check if we can split into <= k subarrays with max sum <= mid
        def can_split(mid: int) -> bool:
            count, curr_sum = 1, 0
            for num in nums:
                if curr_sum + num > mid:
                    count += 1
                    curr_sum = num
                    if count > k:
                        return False
                else:
                    curr_sum += num
            return True
        
        # Binary search for minimum largest sum
        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
nums = [7,2,5,10,8]
k = 2
print(Solution().splitArray(nums, k))  # Output: 18
