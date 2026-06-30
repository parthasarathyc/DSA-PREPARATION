from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices
        result = []

        for i in range(len(nums)):
            # Remove indices out of the current window
            if dq and dq[0] == i - k:
                dq.popleft()

            # Remove smaller elements (they can't be max if current is bigger)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Add to result once the first window is formed
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  
# Output: [3,3,5,5,6,7]

print(sol.maxSlidingWindow([1], 1))  
# Output: [1]
