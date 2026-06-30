'''LeetCode 85. Maximal Rectangle (Python)
Approach: Histogram + Monotonic Stack (Optimal)

Idea:

Treat each row as the base of a histogram.
Update the histogram heights row by row.
For each row, solve Largest Rectangle in Histogram (LeetCode 84).
Keep track of the maximum area.

Time Complexity: O(m × n)
Space Complexity: O(n)

Python Solution'''
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:
            # Build histogram
            for i in range(cols):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0

            max_area = max(max_area, self.largestRectangle(heights))

        return max_area

    def largestRectangle(self, heights):
        stack = []
        max_area = 0
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

        heights.pop()
        return max_area
