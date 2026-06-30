from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        max_len = 0
        seen = {0: -1}  # prefix_sum -> earliest index
        
        for i, num in enumerate(nums):
            prefix_sum += num
            
            if prefix_sum - k in seen:
                max_len = max(max_len, i - seen[prefix_sum - k])
            
            if prefix_sum not in seen:
                seen[prefix_sum] = i
        
        return max_len
sol = Solution()
print(sol.maxSubArrayLen([1, -1, 5, -2, 3], 3))  
# Output: 4  (subarray [1, -1, 5, -2])

print(sol.maxSubArrayLen([-2, -1, 2, 1], 1))  
# Output: 2  (subarray [-1, 2])
