'''LeetCode 402. Remove K Digits (Python)
Approach: Monotonic Increasing Stack (Greedy)

Idea:

Use a stack to build the smallest possible number.
If the current digit is smaller than the top of the stack and k > 0, remove the larger digit.
After processing all digits, if k is still greater than 0, remove digits from the end.
Remove leading zeros and return "0" if the result is empty.

Time Complexity: O(n)
Space Complexity: O(n)

Python Solution'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # Remove remaining digits from the end
        while k > 0:
            stack.pop()
            k -= 1

        # Remove leading zeros
        result = ''.join(stack).lstrip('0')

        return result if result else "0"
