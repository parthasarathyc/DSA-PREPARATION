from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        # Step 1: Precompute window sums
        window_sum = [0] * (n - k + 1)
        curr_sum = sum(nums[:k])
        window_sum[0] = curr_sum
        for i in range(1, n - k + 1):
            curr_sum += nums[i + k - 1] - nums[i - 1]
            window_sum[i] = curr_sum
        
        # Step 2: Best left subarray index up to each position
        left = [0] * len(window_sum)
        best = 0
        for i in range(len(window_sum)):
            if window_sum[i] > window_sum[best]:
                best = i
            left[i] = best
        
        # Step 3: Best right subarray index from each position
        right = [0] * len(window_sum)
        best = len(window_sum) - 1
        for i in range(len(window_sum) - 1, -1, -1):
            if window_sum[i] >= window_sum[best]:
                best = i
            right[i] = best
        
        # Step 4: Try middle subarray and combine with best left/right
        max_total = 0
        ans = []
        for mid in range(k, len(window_sum) - k):
            l, r = left[mid - k], right[mid + k]
            total = window_sum[l] + window_sum[mid] + window_sum[r]
            if total > max_total:
                max_total = total
                ans = [l, mid, r]
        
        return ans
    
sol = Solution()
print(sol.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2))  
# Output: [0, 3, 5]

print(sol.maxSumOfThreeSubarrays([4,5,10,6,11,17,4,5,6], 1))  
# Example output depends on sums

