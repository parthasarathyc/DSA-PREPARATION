from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for current in intervals[1:]:
            prev = merged[-1]
            
            if current[0] <= prev[1]:
                # Overlap → merge
                prev[1] = max(prev[1], current[1])
            else:
                # No overlap → add new interval
                merged.append(current)
        
        return merged
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(intervals))  # Output: [[1,6],[8,10],[15,18]]
