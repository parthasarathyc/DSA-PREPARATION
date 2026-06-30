'''LeetCode 1425. Constrained Subsequence Sum (Python)
Approach: Dynamic Programming + Monotonic Deque (Optimal)

Idea:

Let dp[i] be the maximum subsequence sum ending at index i.

Formula:

dp[i] = nums[i] + max(0, maximum dp value in last k indices)
Use a deque to maintain indices with maximum dp values in the last k positions.

Time Complexity: O(n)
Space Complexity: O(n)

Python Solution'''
from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums, k):
        n = len(nums)
        dp = [0] * n
        dq = deque()
        ans = nums[0]

        for i in range(n):
            # Maximum DP value within last k elements
            if dq:
                dp[i] = nums[i] + max(0, dp[dq[0]])
            else:
                dp[i] = nums[i]

            ans = max(ans, dp[i])

            # Remove smaller DP values
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()

            # Add current index if dp is positive
            if dp[i] > 0:
                dq.append(i)

            # Remove indices outside window
            if dq and dq[0] <= i - k:
                dq.popleft()

        return ans