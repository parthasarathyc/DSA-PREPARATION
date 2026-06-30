'''LeetCode 84. Largest Rectangle in Histogram (Python)
Approach: Monotonic Stack (Optimal)

Time Complexity: O(n)
Space Complexity: O(n)

Python Solution'''''
class Solution:
    def largestRectangleArea(self, heights):
        stack = []  # stores indices
        max_area = 0

        # Add a dummy bar of height 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                max_area = max(max_area, h * width)

            stack.append(i)

        return max_area