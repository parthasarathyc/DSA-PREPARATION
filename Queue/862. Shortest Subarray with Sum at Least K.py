'''LeetCode 862. Shortest Subarray with Sum at Least K (Python)
Approach: Prefix Sum + Monotonic Deque (Optimal)

Idea:

Compute the prefix sum array.
Use a deque to store indices of prefix sums in increasing order.
For each prefix sum:
Check if the current prefix sum minus the smallest prefix sum in the deque is at least k.
If yes, update the shortest length.
Remove larger prefix sums from the back since they are not useful.

Time Complexity: O(n)
Space Complexity: O(n)

Python Solution'''
from collections import deque

class Solution:
    def shortestSubarray(self, nums, k):
        n = len(nums)

        # Prefix Sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dq = deque()
        ans = n + 1

        for i in range(n + 1):
            # Check if current prefix forms a valid subarray
            while dq and prefix[i] - prefix[dq[0]] >= k:
                ans = min(ans, i - dq.popleft())

            # Maintain increasing prefix sums
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()

            dq.append(i)

        return ans if ans <= n else -1
'''Example

Input

nums = [2, -1, 2]
k = 3

Output

3
Dry Run
Prefix Sum
nums   = [2, -1, 2]
prefix = [0, 2, 1, 3]
i	Prefix	Deque	Shortest Length
0	0	[0]	∞
1	2	[0,1]	∞
2	1	[0,2]	∞
3	3	3−0=3 ≥ k → length=3	3

Final Answer:

3
Another Example

Input

nums = [1]
k = 1

Output

1
Interview Explanation
Compute the prefix sum array.
Store indices of prefix sums in a monotonic increasing deque.
For each prefix sum:
While the difference between the current prefix sum and the smallest prefix sum in the deque is at least k, update the answer.
Remove larger prefix sums from the back because a smaller prefix sum is always better for future calculations.
If no valid subarray exists, return -1.
Driver Code
nums = list(map(int, input().split()))
k = int(input())

sol = Solution()
print(sol.shortestSubarray(nums, k))
Sample Input
2 -1 2
3
Sample Output
3
This is the optimal O(n) solution using Prefix Sum + Monotonic Deque, which is the expected approach in coding interviews and on LeetCode.'''