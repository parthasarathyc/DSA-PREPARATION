'''LeetCode 1696. Jump Game VI (Python)
Approach: Dynamic Programming + Monotonic Deque (Optimal)

Idea:

Let dp[i] be the maximum score to reach index i.

Formula:

dp[i] = nums[i] + max(dp[j]) where i-k ≤ j < i
Use a monotonic deque to efficiently maintain the maximum dp value in the last k indices.

Time Complexity: O(n)
Space Complexity: O(n)

Python Solution'''
from collections import deque

class Solution:
    def maxResult(self, nums, k):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        dq = deque([0])

        for i in range(1, n):
            # Remove indices outside the window
            while dq and dq[0] < i - k:
                dq.popleft()

            # Maximum score to reach i
            dp[i] = nums[i] + dp[dq[0]]

            # Maintain decreasing dp values
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()

            dq.append(i)

        return dp[-1]