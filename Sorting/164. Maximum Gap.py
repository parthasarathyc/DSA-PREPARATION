from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0
        
        n = len(nums)
        # Minimum possible gap
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        # Initialize buckets
        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]
        
        # Place numbers into buckets
        for num in nums:
            idx = (num - min_val) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)
        
        # Scan buckets to find maximum gap
        max_gap = 0
        prev_max = min_val
        for b_min, b_max in buckets:
            if b_min == float('inf'):
                continue
            max_gap = max(max_gap, b_min - prev_max)
            prev_max = b_max
        
        return max_gap
nums = [3,6,9,1]
print(Solution().maximumGap(nums))  # Output: 3
