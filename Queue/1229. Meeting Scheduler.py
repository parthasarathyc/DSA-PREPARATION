'''LeetCode 1229. Meeting Scheduler (Python)
Approach: Sort + Two Pointers

Time Complexity: O(n log n + m log m)
Space Complexity: O(1)
'''
class Solution:
    def minAvailableDuration(self, slots1, slots2, duration):
        slots1.sort()
        slots2.sort()

        i = 0
        j = 0

        while i < len(slots1) and j < len(slots2):
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])

            if end - start >= duration:
                return [start, start + duration]

            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1

        return []