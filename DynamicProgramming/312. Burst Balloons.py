from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add virtual balloons
        nums = [1] + nums + [1]
        n = len(nums)
        
        # DP table
        dp = [[0] * n for _ in range(n)]
        
        # length of interval
        for length in range(2, n):  # at least 2 apart
            for left in range(0, n - length):
                right = left + length
                for i in range(left+1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][i] + dp[i][right] + nums[left]*nums[i]*nums[right]
                    )
        
        return dp[0][n-1]
sol = Solution()
print(sol.maxCoins([3,1,5,8]))
# Output: 167
# Explanation: Best order is burst 1 → 5 → 3 → 8

print(sol.maxCoins([1,5]))
# Output: 10
