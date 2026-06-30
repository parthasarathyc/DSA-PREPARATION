from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix_sum = 0
        prefix_map = defaultdict(int)
        prefix_map[0] = 1  # base case: sum = 0
        
        for num in nums:
            prefix_sum += num
            # If (prefix_sum - k) exists, then a subarray ending here sums to k
            count += prefix_map[prefix_sum - k]
            prefix_map[prefix_sum] += 1
        
        return count
nums = [1,2,3]
k = 3
print(Solution().subarraySum(nums, k))  # Output: 2
